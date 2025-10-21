"""
RAG 处理器
实现任务 1-5：论文加载、分割、向量化、存储和相关性分析
"""
import json
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
        self.embeddings = OpenAIEmbeddings(
            model=config.EMBEDDING_MODEL,
            openai_api_key=config.EMBEDDING_API_KEY,
            openai_api_base=config.EMBEDDING_API_BASE
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
        
        # 创建或加载向量数据库
        self.vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            collection_name=config.CHROMA_COLLECTION_NAME,
            persist_directory=self.persist_directory
        )
        
        print(f"✓ Vector store created with {len(chunks)} embeddings")
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
            # 检索该论文的所有块
            results = self.vectorstore.similarity_search(
                query="",
                k=50,
                filter={"paper_id": paper_id}
            )
            paper_text = "\n\n".join([doc.page_content for doc in results])
        
        # 创建总结 prompt
        summary_prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert academic paper summarizer. Provide concise and accurate summaries."),
            ("user", """Please summarize the following research paper in English. Include:
1. Main research question/objective
2. Key methods and approaches
3. Main findings and contributions
4. Significance and impact

Paper content:
{paper_content}

Provide a structured summary in 200-300 words.""")
        ])
        
        # 生成总结
        chain = summary_prompt | self.llm
        response = chain.invoke({"paper_content": paper_text[:4000]})  # 限制长度
        
        summary = {
            "paper_id": paper_id,
            "summary": response.content,
            "generated_at": datetime.now().isoformat()
        }
        
        print(f"✓ Summary generated")
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
        
        # 检索相关文本块（仅限该论文）
        retriever = self.vectorstore.as_retriever(
            search_kwargs={
                "k": top_k,
                "filter": {"paper_id": paper_id}
            }
        )
        
        relevant_chunks = retriever.invoke(question)
        
        # 同时获取相似度分数
        results_with_scores = self.vectorstore.similarity_search_with_score(
            query=question,
            k=top_k,
            filter={"paper_id": paper_id}
        )
        
        # 计算平均相似度分数（Chroma 返回的是距离，越小越相似）
        if results_with_scores:
            avg_distance = sum(score for _, score in results_with_scores) / len(results_with_scores)
            # 转换为相似度分数 (0-1)，距离越小分数越高
            similarity_score = max(0, min(1, 1 - avg_distance / 2))
        else:
            similarity_score = 0.0
        
        # 准备上下文
        context = "\n\n---\n\n".join([doc.page_content for doc in relevant_chunks[:3]])
        
        # 创建分析 prompt
        analysis_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert academic reviewer. Analyze the relevance of research paper content to specific questions.
Provide a JSON response with the following structure:
{{
  "score": <float 0-1>,
  "confidence": <float 0-1>,
  "evidence": "<key evidence from the paper>",
  "reasoning": "<explanation of the relevance>"
}}"""),
            ("user", """Question: {question}

Relevant paper content:
{context}

Based on the above content, evaluate how well this paper addresses the question. 
Consider the similarity score from vector search: {similarity_score:.3f}

Provide your analysis in JSON format.""")
        ])
        
        # 创建 JSON 解析器
        json_parser = JsonOutputParser()
        
        # 创建链
        chain = analysis_prompt | self.llm | json_parser
        
        # 执行分析
        try:
            analysis = chain.invoke({
                "question": question,
                "context": context,
                "similarity_score": similarity_score
            })
            
            # 确保包含所有必需字段
            result = {
                "score": float(analysis.get("score", 0)),
                "confidence": float(analysis.get("confidence", 0)),
                "evidence": analysis.get("evidence", ""),
                "reasoning": analysis.get("reasoning", ""),
                "similarity_score": similarity_score,
                "question_weight": question_weight,
                "chunks_analyzed": len(relevant_chunks)
            }
            
        except Exception as e:
            print(f"⚠️  Error in LLM analysis: {e}")
            # 降级方案：仅使用相似度分数
            result = {
                "score": similarity_score,
                "confidence": 0.5,
                "evidence": context[:200] + "..." if context else "",
                "reasoning": f"Analysis based on similarity score only due to error: {str(e)}",
                "similarity_score": similarity_score,
                "question_weight": question_weight,
                "chunks_analyzed": len(relevant_chunks)
            }
        
        print(f"✓ Relevance score: {result['score']:.3f}, Confidence: {result['confidence']:.3f}")
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


if __name__ == "__main__":
    # 测试代码
    processor = PaperRAGProcessor()
    print("RAG Processor initialized successfully!")
