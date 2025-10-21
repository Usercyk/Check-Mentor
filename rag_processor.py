"""
RAG 处理器
实现任务 1-5：论文加载、分割、向量化、存储和相关性分析
"""
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader, UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

import config
from core_questions import CORE_QUESTIONS, get_question, get_question_weight


class PaperRAGProcessor:
    """论文 RAG 处理器"""
    
    def __init__(self, persist_directory: str = None):
        """
        初始化 RAG 处理器
        
        Args:
            persist_directory: Chroma 持久化目录
        """
        self.persist_directory = persist_directory or config.CHROMA_PERSIST_DIRECTORY
        
        # 初始化 Embeddings
        # 使用自定义embeddings类，因为学校的API与langchain不兼容
        from langchain_core.embeddings import Embeddings
        class CustomEmbeddings(Embeddings):
            def __init__(self, api_key, base_url, model):
                self.api_key = api_key
                self.base_url = base_url
                self.model = model
                from openai import OpenAI
                self.client = OpenAI(api_key=api_key, base_url=base_url)
            
            def embed_documents(self, texts):
                # 分批处理以避免请求体过大，API限制批次大小不超过10
                batch_size = 10  # 每批最多10个文本
                all_embeddings = []
                
                for i in range(0, len(texts), batch_size):
                    batch_texts = texts[i:i + batch_size]
                    response = self.client.embeddings.create(input=batch_texts, model=self.model)
                    all_embeddings.extend([data.embedding for data in response.data])
                
                return all_embeddings
            
            def embed_query(self, text):
                response = self.client.embeddings.create(input=[text], model=self.model)
                return response.data[0].embedding
        
        self.embeddings = CustomEmbeddings(
            api_key=config.EMBEDDING_API_KEY,
            base_url=config.EMBEDDING_API_BASE,
            model=config.EMBEDDING_MODEL
        )
        
        # 初始化 LLM
        self.llm = ChatOpenAI(
            model=config.LLM_MODEL,
            openai_api_key=config.OPENAI_API_KEY,
            base_url=config.OPENAI_API_BASE,
            temperature=0.3
        )
        
        # 初始化文本分割器
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE,
            chunk_overlap=config.CHUNK_OVERLAP,
            length_function=len,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        
        # 向量数据库（延迟初始化）
        self.vectorstore: Optional[Chroma] = None
        
    def load_papers_from_directory(self, directory: str, file_type: str = "pdf") -> List[Document]:
        """
        任务 1: 从目录加载论文
        
        Args:
            directory: 论文所在目录
            file_type: 文件类型，支持 "pdf" 或 "md" (markdown)
            
        Returns:
            文档列表
        """
        print(f"📁 Loading papers from: {directory}")
        
        if file_type == "md":
            # 加载 Markdown 文件
            loader = DirectoryLoader(
                directory,
                glob="**/*.md",
                loader_cls=UnstructuredMarkdownLoader,
                show_progress=True,
                use_multithreading=True
            )
        else:
            # 默认加载 PDF 文件
            loader = DirectoryLoader(
                directory,
                glob="**/*.pdf",
                loader_cls=PyPDFLoader,
                show_progress=True,
                use_multithreading=True
            )
        
        documents = loader.load()
        print(f"✓ Loaded {len(documents)} pages from {file_type.upper()} papers")
        
        return documents
    
    def load_single_paper(self, paper_path: str, paper_metadata: Dict[str, Any]) -> List[Document]:
        """
        加载单篇论文并添加元数据（自动识别 PDF 或 Markdown）
        
        Args:
            paper_path: 论文文件路径（PDF 或 Markdown）
            paper_metadata: 论文元数据（id, title, authors, year等）
            
        Returns:
            带元数据的文档列表
        """
        print(f"📄 Loading paper: {paper_metadata.get('title', 'Unknown')}")
        
        # 根据文件扩展名选择加载器
        if paper_path.lower().endswith('.md'):
            loader = UnstructuredMarkdownLoader(paper_path)
        else:
            loader = PyPDFLoader(paper_path)
        
        documents = loader.load()
        
        # 为每个页面添加论文元数据
        for doc in documents:
            doc.metadata.update(paper_metadata)
        
        print(f"✓ Loaded {len(documents)} pages/sections")
        return documents
    
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """
        任务 2: 将文档分割成块
        
        Args:
            documents: 原始文档列表
            
        Returns:
            分割后的文档块列表
        """
        print(f"✂️  Splitting {len(documents)} documents into chunks...")
        
        chunks = self.text_splitter.split_documents(documents)
        
        print(f"✓ Created {len(chunks)} chunks")
        return chunks
    
    def create_vectorstore(self, chunks: List[Document]) -> Chroma:
        """
        任务 3-4: 向量化并存储到 Chroma
        
        Args:
            chunks: 文档块列表
            
        Returns:
            Chroma 向量数据库实例
        """
        print(f"🔢 Creating vector embeddings and storing in Chroma...")
        print(f"   Persist directory: {self.persist_directory}")
        
        # 清理文档内容：移除空文本和特殊字符
        cleaned_chunks = []
        for chunk in chunks:
            # 确保 page_content 是字符串且不为空
            if hasattr(chunk, 'page_content') and isinstance(chunk.page_content, str):
                content = chunk.page_content.strip()
                if content and len(content) > 0:
                    # 移除可能导致问题的字符
                    content = content.replace('\x00', '')  # 移除空字符
                    if content:
                        # 手动过滤复杂的metadata
                        metadata = chunk.metadata if hasattr(chunk, 'metadata') else {}
                        filtered_metadata = {}
                        for key, value in metadata.items():
                            if isinstance(value, (str, int, float, bool)) or value is None:
                                filtered_metadata[key] = value
                            # 跳过列表和其他复杂类型
                        
                        # 创建新的 Document 对象with cleaned content
                        from langchain_core.documents import Document
                        cleaned_chunk = Document(
                            page_content=content,
                            metadata=filtered_metadata
                        )
                        cleaned_chunks.append(cleaned_chunk)
                else:
                    print(f"⚠️  Skipping chunk with empty content")
            else:
                print(f"⚠️  Skipping chunk with invalid page_content: type={type(chunk.page_content)}")
        
        print(f"   Cleaned: {len(cleaned_chunks)}/{len(chunks)} valid chunks")
        
        if not cleaned_chunks:
            raise ValueError("No valid chunks after cleaning!")
        
        # 创建或加载向量数据库
        self.vectorstore = Chroma.from_documents(
            documents=cleaned_chunks,
            embedding=self.embeddings,
            collection_name=config.CHROMA_COLLECTION_NAME,
            persist_directory=self.persist_directory
        )
        
        print(f"✓ Vector store created with {len(cleaned_chunks)} embeddings")
        return self.vectorstore
    
    def load_vectorstore(self) -> Chroma:
        """
        加载已存在的向量数据库
        
        Returns:
            Chroma 向量数据库实例
        """
        print(f"📚 Loading existing vector store from: {self.persist_directory}")
        
        self.vectorstore = Chroma(
            collection_name=config.CHROMA_COLLECTION_NAME,
            embedding_function=self.embeddings,
            persist_directory=self.persist_directory
        )
        
        print(f"✓ Vector store loaded")
        return self.vectorstore
    
    def add_papers_to_vectorstore(self, chunks: List[Document]):
        """
        向现有向量库添加新论文
        
        Args:
            chunks: 新的文档块列表
        """
        if self.vectorstore is None:
            self.load_vectorstore()
        
        print(f"➕ Adding {len(chunks)} new chunks to vector store...")
        self.vectorstore.add_documents(chunks)
        print(f"✓ Added successfully")
    
    def summarize_paper(self, paper_id: str, paper_text: str = None) -> Dict[str, Any]:
        """
        任务 1 (扩展): 总结单篇论文
        
        Args:
            paper_id: 论文 ID
            paper_text: 论文全文（可选，如不提供则从向量库检索）
            
        Returns:
            包含总结的字典
        """
        print(f"📝 Summarizing paper: {paper_id}")
        
        # 如果没有提供论文全文，从向量库检索相关内容
        if paper_text is None and self.vectorstore is not None:
            # 优先检索论文主要内容（abstract, introduction等），避免作者简介
            # 先尝试获取高质量块（排除bio相关内容）
            main_content_results = self.vectorstore.similarity_search(
                query="research methods findings results conclusion abstract introduction",
                k=20,
                filter={"id": paper_id}  # 使用正确的元数据字段
            )
            
            # 过滤掉可能包含作者简介的块
            filtered_chunks = []
            for doc in main_content_results:
                content = doc.page_content.lower()
                # 排除包含作者信息、致谢、参考文献等非核心内容的块
                if not any(keyword in content for keyword in [
                    'author', 'biography', 'bio:', 'acknowledgment', 'reference', 'citation',
                    'corresponding author', 'email:', 'affiliation', 'department'
                ]):
                    filtered_chunks.append(doc)
            
            # 如果过滤后块太少，补充一些块但标记为低质量
            if len(filtered_chunks) < 5:
                additional_results = self.vectorstore.similarity_search(
                    query="",
                    k=30,
                    filter={"id": paper_id}  # 使用正确的元数据字段
                )
                # 添加未被过滤掉的块
                for doc in additional_results:
                    if doc not in filtered_chunks:
                        filtered_chunks.append(doc)
                        if len(filtered_chunks) >= 10:
                            break
            
            paper_text = "\n\n".join([doc.page_content for doc in filtered_chunks[:15]])  # 限制块数量
        
        # 如果仍然没有内容，返回失败状态
        if not paper_text or len(paper_text.strip()) < 100:
            return {
                "paper_id": paper_id,
                "summary": "Unable to generate summary: insufficient paper content available",
                "generated_at": datetime.now().isoformat(),
                "status": "failed",
                "reason": "insufficient_content"
            }
        
        # 创建总结 prompt
        summary_prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert academic paper summarizer. Provide concise and accurate summaries. If the content is insufficient or appears to be about author biography rather than research content, clearly state this limitation."),
            ("user", """Please summarize the following research paper in English. Include:
1. Main research question/objective
2. Key methods and approaches
3. Main findings and contributions
4. Significance and impact

Paper content:
{paper_content}

Provide a structured summary in 200-300 words. If this appears to be author biography or insufficient research content, please note this clearly.""")
        ])
        
        # 生成总结
        chain = summary_prompt | self.llm
        response = chain.invoke({"paper_content": paper_text[:6000]})  # 增加长度限制
        
        summary_text = response.content.strip()
        
        # 检测占位文本或低质量总结
        placeholder_indicators = [
            "please provide", "i need more", "insufficient", "cannot summarize",
            "not enough information", "unable to", "content appears to be"
        ]
        
        is_placeholder = any(indicator in summary_text.lower() for indicator in placeholder_indicators)
        
        # 如果检测到占位文本，尝试重试一次使用更多上下文
        if is_placeholder and len(filtered_chunks) > 15:
            print("⚠️ Detected placeholder summary, retrying with more context...")
            extended_text = "\n\n".join([doc.page_content for doc in filtered_chunks[:25]])
            response = chain.invoke({"paper_content": extended_text[:8000]})
            summary_text = response.content.strip()
            
            # 再次检查
            is_placeholder = any(indicator in summary_text.lower() for indicator in placeholder_indicators)
        
        summary = {
            "paper_id": paper_id,
            "summary": summary_text,
            "generated_at": datetime.now().isoformat(),
            "status": "success" if not is_placeholder else "warning",
            "chunks_used": len(filtered_chunks) if 'filtered_chunks' in locals() else 0,
            "content_quality": "high" if not is_placeholder else "low"
        }
        
        print(f"✓ Summary generated (status: {summary['status']})")
        return summary
    
    def analyze_paper_relevance(
        self, 
        paper_id: str, 
        question_key: str,
        top_k: int = 5
    ) -> Dict[str, Any]:
        """
        任务 5: 分析论文与特定问题的相关性
        
        Args:
            paper_id: 论文 ID
            question_key: 核心问题的键值
            top_k: 检索的文本块数量
            
        Returns:
            相关性分析结果
        """
        if self.vectorstore is None:
            raise ValueError("Vector store not initialized. Please load or create it first.")
        
        # 获取问题文本
        question = get_question(question_key, language="en")
        question_weight = get_question_weight(question_key)
        
        print(f"🔍 Analyzing relevance for question: {question_key}")
        
        # 检索相关文本块（仅限该论文）- 改进查询以优先获取研究内容
        # 使用更具体的查询，避免匹配参考文献
        retriever = self.vectorstore.as_retriever(
            search_kwargs={
                "k": top_k,
                "filter": {"id": paper_id}  # 使用正确的元数据字段
            }
        )
        
        research_queries = [
            f"{question} research methods results analysis",
            f"{question} experiment theory findings",
            f"{question} abstract introduction conclusion"
        ]
        
        all_relevant_chunks = []
        seen_contents = set()
        
        for query in research_queries:
            try:
                chunks = retriever.invoke(query)
                for chunk in chunks:
                    content = chunk.page_content.strip()
                    # 去重并过滤明显是参考文献的内容
                    if content not in seen_contents and len(content) > 50:
                        # 过滤掉明显的参考文献条目
                        if not (content.count('et al.') > 2 or content.startswith(('1.', '2.', '3.', '['))):
                            all_relevant_chunks.append(chunk)
                            seen_contents.add(content)
                            if len(all_relevant_chunks) >= top_k:
                                break
                if len(all_relevant_chunks) >= top_k:
                    break
            except Exception as e:
                print(f"⚠️ Query failed: {query}, error: {e}")
                continue
        
        # 如果没有找到足够的研究内容，回退到原始查询
        if len(all_relevant_chunks) < 3:
            print("⚠️ Insufficient research content found, falling back to general query")
            fallback_chunks = retriever.invoke(question)
            for chunk in fallback_chunks:
                content = chunk.page_content.strip()
                if content not in seen_contents and len(content) > 50:
                    all_relevant_chunks.append(chunk)
                    seen_contents.add(content)
                    if len(all_relevant_chunks) >= top_k:
                        break
        
        relevant_chunks = all_relevant_chunks[:top_k]
        
        # 同时获取相似度分数
        results_with_scores = self.vectorstore.similarity_search_with_score(
            query=question,
            k=top_k,
            filter={"id": paper_id}  # 使用正确的元数据字段
        )
        
        # 计算平均相似度分数（Chroma 返回的是距离，越小越相似）
        if results_with_scores:
            avg_distance = sum(score for _, score in results_with_scores) / len(results_with_scores)
            # 转换为相似度分数 (0-1)，距离越小分数越高
            similarity_score = max(0, min(1, 1 - avg_distance / 2))
        else:
            similarity_score = 0.0
        
        # 分析块的来源类型，用于确定推理水平
        chunk_sources = []
        for doc in relevant_chunks:
            content = doc.page_content.lower()
            # 改进关键词匹配，优先识别研究内容
            has_research_keywords = any(keyword in content for keyword in [
                'abstract', 'introduction', 'method', 'methods', 'result', 'results', 
                'conclusion', 'conclusions', 'experiment', 'experimental', 'theory',
                'analysis', 'discussion', 'figure', 'fig.', 'table', 'algorithm'
            ])
            has_bio_keywords = any(keyword in content for keyword in [
                'author', 'biography', 'bio:', 'acknowledgment', 'acknowledgements',
                'affiliation', 'department', 'corresponding author', 'email:', 'funding'
            ])
            has_reference_keywords = any(keyword in content for keyword in [
                'et al.', 'phys. rev.', 'nature', 'science', 'arxiv:', 'doi:', 'vol.', 'pp.'
            ])
            
            if has_research_keywords:
                chunk_sources.append("research_content")
            elif has_bio_keywords:
                chunk_sources.append("author_bio")
            elif has_reference_keywords:
                chunk_sources.append("references")
            else:
                chunk_sources.append("other")
        
        # 确定推理水平 - 改进逻辑
        research_count = chunk_sources.count("research_content")
        bio_count = chunk_sources.count("author_bio")
        ref_count = chunk_sources.count("references")
        
        if research_count > 0:
            inference_level = "direct_evidence"
        elif bio_count > 0 and research_count == 0:
            inference_level = "inferred_from_bio"
        elif ref_count > 0 and research_count == 0 and bio_count == 0:
            inference_level = "inferred_from_references"
        else:
            inference_level = "weak_inference"
        
        # 准备上下文
        context = "\n\n---\n\n".join([doc.page_content for doc in relevant_chunks[:3]])
        
        # 构建去重的chunks_used列表
        seen_contents = set()
        unique_chunks_used = []
        for i, doc in enumerate(relevant_chunks[:3]):
            content = doc.page_content
            if content not in seen_contents:
                seen_contents.add(content)
                score = next((score for d, score in results_with_scores if d.page_content == content), None)
                unique_chunks_used.append({
                    "preview": content[:200] + "..." if len(content) > 200 else content,
                    "similarity_score": score,
                    "source_type": chunk_sources[i] if i < len(chunk_sources) else "unknown"
                })
        
        # 限制为最多3个唯一块
        unique_chunks_used = unique_chunks_used[:3]
        analysis_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert academic reviewer specializing in analyzing research papers and professor profiles. 
Your task is to analyze how well a research paper contributes to understanding a professor's research interests and the broader field.

Provide a comprehensive but accessible analysis that is scientifically rigorous yet easy to understand. 
Focus on key insights, practical implications, and educational value.

If the content appears to be from author biography rather than research content, you may still make reasonable inferences about potential research directions, but clearly indicate this uncertainty.

Provide a JSON response with the following structure:
{{
  "score": <float 0-1, how relevant this paper is to the question>,
  "confidence": <float 0-1, your confidence in this assessment>,
  "evidence": "<key evidence from the paper, explained clearly>",
  "reasoning": "<comprehensive explanation that is simple but scientifically accurate>",
  "inference_level": "<direct_evidence|inferred_from_bio|weak_inference>"
}}"""),
            ("user", """Question: {question}

Relevant paper content:
{context}

Based on the above content, evaluate how well this paper helps answer the question. 
Consider the similarity score from vector search: {similarity_score:.3f}

Content source analysis: {inference_level_desc}

Provide your analysis in JSON format. Make your explanation comprehensive yet accessible, scientifically rigorous but not overly technical. If using biographical information, clearly note the inferential nature of your analysis.""")
        ])
        
        # 创建 JSON 解析器
        json_parser = JsonOutputParser()
        
        # 创建链
        chain = analysis_prompt | self.llm | json_parser
        
        # 准备推理水平描述
        inference_descriptions = {
            "direct_evidence": "Content appears to be from research sections (abstract, methods, results, etc.)",
            "inferred_from_bio": "Content appears to be from author biography - analysis is inferential",
            "weak_inference": "Content source unclear - analysis has higher uncertainty"
        }
        inference_level_desc = inference_descriptions.get(inference_level, "Content source analysis unavailable")
        
        # 执行分析
        try:
            analysis = chain.invoke({
                "question": question,
                "context": context,
                "similarity_score": similarity_score,
                "inference_level_desc": inference_level_desc
            })
            
            # 确保包含所有必需字段
            result = {
                "score": float(analysis.get("score", 0)),
                "confidence": float(analysis.get("confidence", 0)),
                "evidence": analysis.get("evidence", ""),
                "reasoning": analysis.get("reasoning", ""),
                "inference_level": analysis.get("inference_level", inference_level),
                "similarity_score": similarity_score,
                "question_weight": question_weight,
                "chunks_analyzed": len(relevant_chunks),
                "chunks_used": unique_chunks_used
            }
            
        except Exception as e:
            print(f"⚠️  Error in LLM analysis: {e}")
            # 降级方案：仅使用相似度分数
            result = {
                "score": similarity_score,
                "confidence": 0.5,
                "evidence": context[:200] + "..." if context else "",
                "reasoning": f"Analysis based on similarity score only due to error: {str(e)}",
                "inference_level": inference_level,
                "similarity_score": similarity_score,
                "question_weight": question_weight,
                "chunks_analyzed": len(relevant_chunks),
                "chunks_used": unique_chunks_used
            }
        
        print(f"✓ Relevance score: {result['score']:.3f}, Confidence: {result['confidence']:.3f}, Inference: {result['inference_level']}")
        return result
    
    def analyze_all_questions_for_paper(self, paper_id: str) -> Dict[str, Dict[str, Any]]:
        """
        分析论文对所有核心问题的相关性
        
        Args:
            paper_id: 论文 ID
            
        Returns:
            完整的相关性分析结果
        """
        print(f"\n{'='*70}")
        print(f"📊 Analyzing paper {paper_id} for all core questions")
        print(f"{'='*70}\n")
        
        relevance_analysis = {}
        
        for question_key in CORE_QUESTIONS.keys():
            analysis = self.analyze_paper_relevance(paper_id, question_key)
            relevance_analysis[question_key] = analysis
        
        print(f"\n✓ Complete analysis for paper {paper_id}")
        return relevance_analysis
    
    def process_papers_batch(
        self, 
        papers_info: List[Dict[str, Any]], 
        paper_directory: str,
        file_type: str = "pdf"
    ) -> Dict[str, Any]:
        """
        批量处理论文（完整流程：加载 -> 分割 -> 向量化 -> 分析）
        
        Args:
            papers_info: 论文信息列表，每项包含 id, title, authors, year, pdf_filename/md_filename
            paper_directory: 论文文件所在目录
            file_type: 文件类型，支持 "pdf" 或 "md" (markdown)
            
        Returns:
            包含所有分析结果的字典
        """
        paper_dir = Path(paper_directory)
        all_chunks = []
        summaries = {}
        analysis_results = {}
        
        # 确定文件扩展名和字段名
        file_ext = "pdf" if file_type == "pdf" else "md"
        filename_key = "pdf_filename" if file_type == "pdf" else "md_filename"
        
        # 步骤 1-2: 加载并分割所有论文
        for paper_info in papers_info:
            paper_id = paper_info['id']
            # 支持两种字段名
            paper_filename = paper_info.get(filename_key, paper_info.get('pdf_filename', f"{paper_id}.{file_ext}"))
            paper_path = paper_dir / paper_filename
            
            if not paper_path.exists():
                print(f"⚠️  File not found: {paper_path}")
                continue
            
            # 加载论文（对于 PDF 和 Markdown，load_single_paper 会自动处理）
            documents = self.load_single_paper(str(paper_path), paper_info)
            
            # 分割文档
            chunks = self.split_documents(documents)
            all_chunks.extend(chunks)
        
        # 步骤 3-4: 创建向量库
        self.create_vectorstore(all_chunks)
        
        # 步骤 5: 对每篇论文进行相关性分析
        for paper_info in papers_info:
            paper_id = paper_info['id']
            
            # 生成总结
            try:
                summary = self.summarize_paper(paper_id)
                summaries[paper_id] = summary
            except Exception as e:
                print(f"⚠️  Error summarizing paper {paper_id}: {e}")
                summaries[paper_id] = {"error": str(e)}
            
            # 分析相关性
            try:
                analysis = self.analyze_all_questions_for_paper(paper_id)
                analysis_results[paper_id] = analysis
            except Exception as e:
                print(f"⚠️  Error analyzing paper {paper_id}: {e}")
                analysis_results[paper_id] = {"error": str(e)}
        
        return {
            "summaries": summaries,
            "analysis_results": analysis_results,
            "total_papers": len(papers_info),
            "total_chunks": len(all_chunks)
        }


# 模块提供 PaperRAGProcessor 类；尾部测试代码已移除以避免导入时副作用
