"""
Workflow 1: 分析教授的核心贡献

该工作流的目标是回答第一个核心问题：
"老师对哪些方向感兴趣，他对此有哪些贡献？"

它通过以下步骤实现：
1. 接收教授的代表作列表（main_papers）作为输入。
2. 对每一篇代表作进行内容总结，提取其核心研究方向和贡献。
3. 将所有论文的分析结果进行综合，形成一个关于教授整体研究方向和贡献的结构化报告。
"""
import json
import time
import re
from typing import List, Dict, Any
from tqdm import tqdm

from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from .. import config
from .cache_manager import CacheManager

class ContributionWorkflow:
    """
    分析教授核心贡献的工作流。
    """
    def __init__(self, main_llm, fallback_llm=None, gemini_llm=None):
        """
        初始化工作流，接收外部传入的LLM实例。
        """
        print("  -> ContributionWorkflow initialized.")
        self.llm = main_llm
        self.fallback_llm = fallback_llm
        self.gemini_llm = gemini_llm
        self.cache = None

    def _load_paper_content(self, file_path: str) -> str:
        """加载指定路径的 Markdown 文件内容。"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"    ⚠️ Error loading file {file_path}: {e}")
            return ""

    def _invoke_llm_with_fallback(self, chain, paper_content, metadata_context=""):
        """
        调用LLM，如果主LLM失败，则尝试备用LLM。
        这是一个通用的调用逻辑，适用于所有单篇论文分析。
        
        Args:
            chain: LangChain链
            paper_content: 论文内容
            metadata_context: 元数据上下文信息
        """
        try:
            # 尝试主LLM (在tqdm模式下保持静默)
            result = chain.invoke({
                "paper_content": paper_content[:12000],
                "metadata_context": metadata_context
            })
            return result
        except (OutputParserException, json.JSONDecodeError):
            # 第一次解析失败，静默重试一次
            try:
                result = chain.invoke({
                    "paper_content": paper_content[:12000],
                    "metadata_context": metadata_context
                })
                return result
            except Exception:
                # 重试失败，交由备用模型处理
                pass
        except Exception:
            # 其他主LLM错误，交由备用模型处理
            pass

        # 如果主LLM失败，且备用LLM已配置，则尝试备用LLM
        if self.fallback_llm:
            try:
                fallback_chain = chain.with_components(llm=self.fallback_llm)
                result = fallback_chain.invoke({
                    "paper_content": paper_content[:12000],
                    "metadata_context": metadata_context
                })
                return result
            except Exception:
                # 备用模型也失败了
                pass
        
        # 如果都失败了，则返回一个错误标记
        return {"error": "Both main and fallback LLMs failed."}


    def _analyze_single_paper(self, paper_content: str, metadata: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        使用 LLM 分析单篇论文的内容，提取研究领域和核心贡献。
        
        Args:
            paper_content: 论文内容
            metadata: 论文元数据（可选），包含发布时间、作者等信息
        """
        # 构建元数据上下文信息
        metadata_context = ""
        if metadata:
            metadata_context = "\n\n**Paper Metadata:**"
            if metadata.get("publish_date"):
                metadata_context += f"\n- Publication Date: {metadata['publish_date']}"
            if metadata.get("authors"):
                metadata_context += f"\n- Authors: {', '.join(metadata['authors'][:5])}"  # 只显示前5位作者
                if len(metadata['authors']) > 5:
                    metadata_context += f" (and {len(metadata['authors']) - 5} more)"
            if metadata.get("doi"):
                metadata_context += f"\n- DOI: {metadata['doi']}"
            
            # 强调新论文的重要性
            recency_note = ""
            if metadata.get("publish_date"):
                try:
                    from datetime import datetime
                    pub_year = int(metadata['publish_date'][:4])
                    current_year = datetime.now().year
                    age = current_year - pub_year
                    
                    if age <= 2:
                        recency_note = "\n\n**NOTE**: This is a very recent paper (published within the last 2 years). Recent papers often represent the cutting-edge of the field and should be given special attention when identifying current research directions."
                    elif age <= 5:
                        recency_note = "\n\n**NOTE**: This is a relatively recent paper. Consider how it reflects current trends in the field."
                except:
                    pass
            
            metadata_context += recency_note
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert academic analyst. Your task is to extract the key information from a research paper.
Provide a JSON response with the following structure:
{{
  "research_area": "<The primary research area or sub-field of this paper, e.g., 'Quantum Computing', 'Photonic Integrated Circuits'>",
  "core_contribution": "<A concise, one-sentence summary of the paper's main contribution.>"
}}"""),
            ("user", "Please analyze the following paper content and provide the structured JSON output:{metadata_context}\n\n---\n{paper_content}\n---")
        ])
        
        parser = JsonOutputParser()
        chain = prompt | self.llm | parser

        analysis_result = self._invoke_llm_with_fallback(
            chain, 
            paper_content,
            metadata_context=metadata_context
        )
        # 在进度条模式下，单个请求的延迟可以适当缩短或移除，
        # 因为总体速率由循环控制
        # time.sleep(1) 
        
        return analysis_result

    def _cluster_papers_by_llm(self, papers: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """
        使用LLM对论文进行语义聚类。
        """
        print("    -> High-quality paper count exceeds threshold. Performing LLM-based semantic clustering...")

        paper_info = [
            {"title": p.get("title", "N/A"), "research_area": p.get("research_area", "N/A"), "core_contribution": p.get("core_contribution", "N/A")}
            for p in papers
        ]

        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a senior research analyst. You have been given a list of papers, each with its title, research area, and core contribution. Your task is to group these papers into 3-5 high-level research themes based on the **semantic similarity** of their research areas and contributions.

Your task is **clustering, not summarization**.

The output MUST be a valid JSON object where:
- Each KEY is a concise, descriptive name for a research theme you identified (e.g., "Quantum Photonic Integration", "Topological Quantum Computing").
- Each VALUE is a list of paper titles that belong to that theme.

Example Input:
[
  {{"title": "Paper A", "research_area": "Quantum Computing", "core_contribution": "scalable quantum entanglement"}},
  {{"title": "Paper B", "research_area": "Quantum Optics", "core_contribution": "multi-photon entangled states"}},
  {{"title": "Paper C", "research_area": "Photonic Chips", "core_contribution": "topological protection on chips"}}
]

Example Output:
{{
  "Quantum Entanglement": ["Paper A", "Paper B"],
  "Topological Photonics": ["Paper C"]
}}"""),
            ("user", "Here is the list of papers to cluster:\n\n{paper_info_json}")
        ])

        parser = JsonOutputParser()
        chain = prompt | self.llm | parser

        try:
            paper_info_json = json.dumps(paper_info, indent=2, ensure_ascii=False)
            cluster_result = chain.invoke({"paper_info_json": paper_info_json})
            return cluster_result
        except Exception as e:
            print(f"    ⚠️ Error during LLM clustering: {e}")
            # Fallback: if clustering fails, return a single group to avoid crashing
            return {"All Papers": [p["title"] for p in papers]}

    def _synthesize_results(self, all_analyses: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        将所有论文的分析结果综合成一个总的、对本科生友好的报告。
        
        现在会考虑论文的时效性权重：更新的论文在综合时会被给予更多关注。
        如果论文过多，会进行聚类和代表性采样。
        """
        # 过滤掉分析失败的论文
        valid_analyses = [analysis for analysis in all_analyses if "error" not in analysis]
        if not valid_analyses:
            return {
                "research_directions": ["No valid analysis results to synthesize."],
                "contribution_summary": "Could not generate a summary due to lack of valid data."
            }

        # 按优先级得分排序（时效性 + 来源权重）
        # 高得分（更新 + 核心来源）的论文会被放在前面
        def get_priority_score(analysis):
            score = analysis.get('recency_score', 0.5)
            # 核心来源（primary）给予额外加权，确保它们排在前面
            if analysis.get('source_type') == 'primary':
                score += 0.3 
            return score
        
        sorted_analyses = sorted(valid_analyses, key=get_priority_score, reverse=True)
        
        # 如果论文过多，进行聚类和代表性采样
        if len(sorted_analyses) > 10:
            print(f"    -> Found {len(sorted_analyses)} papers. Performing clustering and representative sampling...")
            
            # 1. LLM语义聚类
            clusters = self._cluster_papers_by_llm(sorted_analyses)
            
            # 2. 代表性提取：从每个主题中选择优先级最高的论文
            representative_papers = []
            paper_map = {p["title"]: p for p in sorted_analyses}
            
            for theme, titles in clusters.items():
                if not titles: continue
                
                # 找到该主题下优先级得分最高的论文
                theme_papers = [paper_map[title] for title in titles if title in paper_map]
                if not theme_papers: continue
                
                best_paper_in_theme = max(theme_papers, key=get_priority_score)
                representative_papers.append(best_paper_in_theme)
            
            # 去重
            final_papers_for_synthesis = list({p["paper_id"]: p for p in representative_papers}.values())
            print(f"    -> Clustered into {len(clusters)} themes. Selected {len(final_papers_for_synthesis)} representative papers for synthesis.")
            sorted_analyses = final_papers_for_synthesis
        else:
            print(f"    -> Number of papers ({len(sorted_analyses)}) is manageable. Using all for synthesis.")
        
        # 构建分析文本，包含时效性和来源信息
        analysis_parts = []
        for i, analysis in enumerate(sorted_analyses):
            paper_text = f"Paper {i+1}:\n- Research Area: {analysis.get('research_area', 'N/A')}\n- Core Contribution: {analysis.get('core_contribution', 'N/A')}"
            
            # 来源标记
            if analysis.get('source_type') == 'primary':
                paper_text += f"\n- **Status: CORE REPRESENTATIVE WORK** (High Priority - This is a key paper)"
            
            # 如果有时效性信息，添加权重提示
            recency_score = analysis.get('recency_score')
            if recency_score is not None and recency_score != 0.5:  # 0.5是默认值
                if recency_score > 0.8:
                    paper_text += f"\n- **Recency Weight: HIGH** (published recently, represents cutting-edge work)"
                elif recency_score > 0.6:
                    paper_text += f"\n- **Recency Weight: MEDIUM-HIGH** (relatively recent work)"
                elif recency_score < 0.3:
                    paper_text += f"\n- **Recency Weight: LOW** (older foundational work)"
            
            analysis_parts.append(paper_text)
        
        analysis_text = "\n\n".join(analysis_parts)

        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a pragmatic and knowledgeable academic mentor, tasked with writing a summary of a professor's research for a bright, motivated undergraduate student.

**Your Goal:** Transform a list of individual paper analyses into a coherent, educational, and grounded narrative.
**Your Audience:** A smart undergraduate who is familiar with basic concepts but needs a clear guide to this specific field.

**CRITICAL STYLE GUIDELINES:**
1.  **Natural Flow:** Do NOT write a disjointed list of facts. Use transition words (e.g., "Furthermore," "Specifically," "Building on this") to connect ideas smoothly. The text should read like a thoughtful email from a mentor, not a robot-generated report.
2.  **NO HYPE / NO FLUFF:** Strictly avoid exaggerated adjectives like "revolutionary," "unprecedented," or "miraculous." Do not sound like a marketing brochure. Be objective. Instead of saying "He made a groundbreaking discovery," say "He demonstrated [X] for the first time" or "He proposed a method to solve [Y]."
3.  **Clarity over Jargon:** Explain *why* something is done before saying *what* was done.

**IMPORTANT - Weighting Instructions**: 
- **CORE REPRESENTATIVE WORK**: Papers marked with this status are the professor's most important contributions (e.g., PRD, PRL papers). You MUST prioritize these papers in your summary. Ensure their contributions are highlighted prominently.
- **Recency Weight**: Focus the narrative on "HIGH" or "MEDIUM-HIGH" recency papers to reflect current interests. Use older papers only for context.

**Key Instructions:**

1.  **Content - Section 1: Research Directions (What they do):**
    *   Identify 3-5 primary research themes.
    *   For each theme, write a fluid paragraph. Start with the *problem* or *goal*, then describe the *approach*.
    *   **"Prudent Explanation":** If you use a specialized term (e.g., "topological photonics"), briefly explain it in simple terms within parentheses, but only if you are sure. If unsure, use the term as is.

2.  **Content - Section 2: Contribution Summary (The Big Picture):**
    *   Synthesize the individual contributions into a single, flowing narrative (approx. 300-400 words).
    *   **Focus on Concrete Achievements:** What specific problem did they solve? What new capability did they unlock?
    *   **Connect the Dots:** How do these different papers fit together? Is there a central philosophy or methodology?
    *   **Impact:** Describe the impact in terms of scientific progress (e.g., "This work allows for more stable quantum bits"), not just prestige.

**Output Format:**
You MUST provide a JSON response with a `research_directions` key (a list of strings) and a `contribution_summary` key (a single string).

{{
  "research_directions": [
    "<Paragraph for Direction 1>",
    "<Paragraph for Direction 2>",
    ...
  ],
  "contribution_summary": "<The overall summary paragraph. Fluid, objective, and educational.>"
}}"""),
            ("user", "Based on the following analyses of the professor's papers, please generate the structured summary:\n\n---\n{analysis_text}\n---")
        ])

        # 分离LLM调用和解析
        parser = JsonOutputParser()

        # 尝试使用 Gemini (如果配置了)
        raw_output_obj = None
        if self.gemini_llm:
            try:
                print("    -> Attempting synthesis with Gemini...")
                llm_chain = prompt | self.gemini_llm
                raw_output_obj = llm_chain.invoke({"analysis_text": analysis_text})
            except Exception as e:
                print(f"    ⚠️ Gemini synthesis failed (Timeout or Error): {e}")
                print("    -> Falling back to Main LLM (OpenAI)...")
                raw_output_obj = None # Reset to trigger fallback

        # 如果 Gemini 没配置或者失败了，使用主 LLM
        if not raw_output_obj:
            try:
                llm_chain = prompt | self.llm
                raw_output_obj = llm_chain.invoke({"analysis_text": analysis_text})
            except Exception as e:
                print(f"    🔴 Critical Error: Main LLM synthesis also failed: {e}")
                return {
                    "research_directions": ["Synthesis failed."],
                    "contribution_summary": f"Both Gemini and Main LLM failed to synthesize results. Error: {e}"
                }

        try:
            # 步骤1: 获取原始输出 (raw_output_obj 已经获取到了)
            raw_output = raw_output_obj.content if hasattr(raw_output_obj, 'content') else str(raw_output_obj)

            # 步骤2: 清理并提取纯净的JSON字符串
            match = re.search(r"```json\s*([\s\S]*?)\s*```", raw_output)
            if match:
                cleaned_output = match.group(1)
            else:
                cleaned_output = raw_output

            # 步骤3: 尝试解析清理后的输出
            synthesis_result = parser.parse(cleaned_output)
            
            # 步骤4: 验证解析后的结构
            if not isinstance(synthesis_result, dict) or "contribution_summary" not in synthesis_result:
                print(f"    ⚠️ Synthesis output is not in the expected format: {synthesis_result}")
                return {
                    "research_directions": ["Synthesis failed: Unexpected output format."],
                    "contribution_summary": f"LLM returned an unexpected data structure. Raw output: {json.dumps(synthesis_result, indent=2, ensure_ascii=False)}"
                }
            return synthesis_result
            
        except OutputParserException as e:
            print(f"    🔴 Critical Error: Failed to parse LLM output during synthesis. Reason: {e}")
            return {
                "research_directions": ["Synthesis failed: OutputParserException."],
                "contribution_summary": f"The language model's response was not valid JSON and could not be parsed. Raw output snippet: {e.llm_output[:200]}..."
            }
        except Exception as e:
            print(f"    🔴 Critical Error: An unexpected error occurred during synthesis: {e}")
            return {
                "research_directions": ["Synthesis failed: Unexpected Exception."],
                "contribution_summary": f"An unexpected error occurred. Reason: {str(e)}"
            }

    def run(self, professor_name: str, main_papers: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        执行分析教授核心贡献的完整流程。
        """
        self.cache = CacheManager(professor_name, "contribution_analysis")
        print(f"  -> Running ContributionWorkflow on {len(main_papers)} main papers.")

        if not main_papers:
            print("  -> No main papers provided. Skipping workflow.")
            return {
                "summary": "没有提供教授的代表作，无法分析其核心贡献。",
                "research_areas": [],
                "key_contributions": []
            }

        # 步骤1: 对每篇论文进行单独分析
        all_single_analyses = []
        
        # 使用tqdm创建进度条
        for paper in tqdm(main_papers, desc="  -> Analyzing contributions"):
            paper_id = paper['id']
            # 检查缓存，并要求所有关键字段都存在
            cached_result = self.cache.get(
                paper_id, 
                required_keys=["paper_id", "title", "research_area", "core_contribution"]
            )

            if cached_result:
                single_analysis = cached_result
                # 确保缓存的结果也包含时效性得分（如果论文有这个字段）
                if 'recency_score' not in single_analysis and 'recency_score' in paper:
                    single_analysis['recency_score'] = paper['recency_score']
                
                # 即使是缓存结果，也尝试注入最新的元数据(DOI/URL)
                paper_metadata = paper.get('metadata')
                if paper_metadata:
                    if 'doi' not in single_analysis and paper_metadata.get('doi'):
                        single_analysis['doi'] = paper_metadata['doi']
                    if 'inspire_url' not in single_analysis and paper_metadata.get('inspire_url'):
                        single_analysis['inspire_url'] = paper_metadata['inspire_url']
            else:
                content = self._load_paper_content(paper['md_filename'])
                if not content:
                    continue
                
                # 提取元数据
                paper_metadata = paper.get('metadata')
                
                analysis_result = self._analyze_single_paper(content, paper_metadata)
                
                # 检查LLM调用是否出错
                if analysis_result.get("error"):
                    tqdm.write(f"    ⚠️ Skipped paper '{paper['title']}' due to LLM failure.")
                    continue

                # 构建完整的分析对象，包含时效性得分
                single_analysis = {
                    **analysis_result,
                    'paper_id': paper_id,
                    'title': paper['title'],
                    'source_type': paper.get('source_type', 'primary')
                }
                
                # 注入 DOI 和 INSPIRE URL（如果元数据存在）
                if paper_metadata:
                    if paper_metadata.get('doi'):
                        single_analysis['doi'] = paper_metadata['doi']
                    if paper_metadata.get('inspire_url'):
                        single_analysis['inspire_url'] = paper_metadata['inspire_url']
                
                # 如果论文有时效性得分，也包含进去
                if 'recency_score' in paper:
                    single_analysis['recency_score'] = paper['recency_score']
                
                # 缓存完整的对象
                self.cache.set(paper_id, single_analysis)
                time.sleep(1) # 在成功调用后保留延迟，避免API超速

            all_single_analyses.append(single_analysis)

        # 检查是否有任何论文被成功分析
        if not all_single_analyses:
            print("  -> No papers were successfully analyzed. Skipping synthesis.")
            return {
                "summary": "所有论文均未能成功分析，无法生成总结。",
                "research_areas": [],
                "key_contributions": []
            }

        # 步骤2: 综合所有分析结果
        print("\n    -> Synthesizing all results...")
        final_summary = self._synthesize_results(all_single_analyses)

        # 步骤3: 格式化最终输出
        return {
            "research_directions": final_summary.get("research_directions", []),
            "contribution_summary": final_summary.get("contribution_summary", "未能生成核心贡献总结。"),
            "analyzed_papers": all_single_analyses,  # Return full objects to include metadata like DOI/URL
            "key_contributions": [
                {
                    "paper_id": analysis['paper_id'],
                    "title": analysis['title'],
                    "contribution": analysis.get('core_contribution', 'N/A')
                }
                for analysis in all_single_analyses
            ]
        }
