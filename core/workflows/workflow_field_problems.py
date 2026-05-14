"""
Workflow 2: 分析领域的热点问题

该工作流的目标是回答第二个核心问题：
"这个领域主要在关心什么问题？"

它通过以下步骤实现：
1. 接收教授的代表作（main_papers）和关键参考文献（ref1_papers）作为输入。
2. 设计一个AI评分机制，评估每篇论文对于“领域问题代表性”的得分。
3. 基于得分较高的论文，综合分析出该领域当前关注的核心问题和技术趋势。
"""
import json
import time
from typing import List, Dict, Any
from tqdm import tqdm

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from .cache_manager import CacheManager

class FieldProblemsWorkflow:
    """
    分析领域热点问题的工作流。
    """
    def __init__(self, main_llm, fallback_llm=None, gemini_llm=None):
        """
        初始化工作流，接收外部传入的LLM实例。
        """
        print("  -> FieldProblemsWorkflow initialized.")
        self.llm = main_llm
        self.fallback_llm = fallback_llm
        self.gemini_llm = gemini_llm
        self.cache = None

    def _print_section_header(self, title: str, level: int = 1):
        """打印带样式的章节标题"""
        if level == 1:
            print(f"\n{'='*70}\n🎓 {title}\n{'='*70}")
        elif level == 2:
            print(f"\n--- {title} ---")

    def _load_paper_content(self, file_path: str) -> str:
        """加载指定路径的 Markdown 文件内容。"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"    ⚠️ Error loading file {file_path}: {e}")
            return ""

    def _invoke_llm_with_fallback(self, chain, paper_content, metadata_context="", temporal_instruction=""):
        """
        调用LLM，如果主LLM失败，则尝试备用LLM。
        
        Args:
            chain: LangChain链
            paper_content: 论文内容
            metadata_context: 元数据上下文信息
            temporal_instruction: 时间相关的指令
        """
        try:
            result = chain.invoke({
                "paper_content": paper_content[:12000],
                "metadata_context": metadata_context,
                "temporal_instruction": temporal_instruction
            })
            return result
        except (OutputParserException, json.JSONDecodeError):
            try:
                result = chain.invoke({
                    "paper_content": paper_content[:12000],
                    "metadata_context": metadata_context,
                    "temporal_instruction": temporal_instruction
                })
                return result
            except Exception:
                pass
        except Exception:
            pass

        if self.fallback_llm:
            try:
                fallback_chain = chain.with_llm(self.fallback_llm)
                result = fallback_chain.invoke({
                    "paper_content": paper_content[:12000],
                    "metadata_context": metadata_context,
                    "temporal_instruction": temporal_instruction
                })
                return result
            except Exception:
                pass
        
        return {"error": "Both main and fallback LLMs failed."}

    def _rate_single_paper(self, paper_content: str, metadata: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        使用 LLM 评估单篇论文，基于四维模型进行打分。
        
        Args:
            paper_content: 论文内容
            metadata: 论文元数据（可选），包含发布时间、作者等信息
        """
        # 构建元数据上下文
        metadata_context = ""
        temporal_instruction = ""
        
        if metadata:
            metadata_context = "\n\n**Paper Metadata:**"
            if metadata.get("publish_date"):
                metadata_context += f"\n- Publication Date: {metadata['publish_date']}"
                
                # 根据发布时间添加特殊说明
                try:
                    from datetime import datetime
                    pub_year = int(metadata['publish_date'][:4])
                    current_year = datetime.now().year
                    age = current_year - pub_year
                    
                    if age <= 2:
                        temporal_instruction = "\n\n**TEMPORAL CONTEXT**: This is a very recent paper (published within the last 2 years). Recent papers are especially valuable for understanding the field's CURRENT priorities. When evaluating 'Significance' and 'Potential', consider that this represents cutting-edge work that may define emerging directions."
                    elif age <= 5:
                        temporal_instruction = "\n\n**TEMPORAL CONTEXT**: This is a relatively recent paper. It likely reflects current trends in the field."
                    elif age >= 10:
                        temporal_instruction = "\n\n**TEMPORAL CONTEXT**: This is an older paper. While it may be foundational, be careful when using it to assess the field's CURRENT priorities. It's more valuable for historical context than for identifying today's hot topics."
                except:
                    pass
            
            if metadata.get("authors"):
                metadata_context += f"\n- Authors: {', '.join(metadata['authors'][:5])}"
                if len(metadata['authors']) > 5:
                    metadata_context += f" (and {len(metadata['authors']) - 5} more)"
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a research analyst tasked with identifying papers that best reveal **what problems a research field cares about**. Your goal is NOT to judge academic quality, but to assess how well each paper helps us understand the field's current priorities, challenges, and directions.

**CONTEXT**: We are analyzing a collection of high-quality papers to answer: "What are the hot topics and core problems in this field?" Some papers are better "informants" than others for this purpose.

**CRITICAL INSIGHT**: Review papers and perspective articles are often MORE valuable for our purpose than individual research papers, because they:
- Synthesize multiple research directions
- Explain historical context and motivations
- Map out the field's structure and connections
- Identify open challenges and future trends

**Scoring Philosophy**: Use the FULL 0.00-1.00 range. Think: "How much does this paper help me understand the field's priorities?"
- **0.9-1.0**: Exceptional field guide (e.g., comprehensive review that maps the entire landscape)
- **0.7-0.8**: Strong informant (e.g., breakthrough work that defines a new direction, or excellent topical review)
- **0.5-0.6**: Useful contributor (e.g., solid work on a recognized problem)
- **0.3-0.4**: Narrow focus (e.g., incremental advance on a sub-problem)
- **0.0-0.2**: Limited insight (e.g., too specialized or peripheral)

**Evaluate on FOUR dimensions:**

**1. Significance (Weight: 30%)**: How central is the problem to the field's current priorities?
- **0.9-1.0**: Addresses a grand challenge that defines the field (e.g., scalable quantum computing, fault tolerance).
- **0.7-0.8**: Tackles a major recognized problem with broad implications.
- **0.5-0.6**: Works on a well-known, important sub-problem.
- **0.3-0.4**: Addresses a niche or specialized issue.
- **0.0-0.2**: Marginal problem with limited community interest.

**2. Novelty (Weight: 10%)**: How original is the approach?
- **0.9-1.0**: Introduces a paradigm shift or fundamentally new methodology.
- **0.7-0.8**: Highly creative synthesis or major breakthrough.
- **0.5-0.6**: Clever improvement or novel application.
- **0.3-0.4**: Standard extension of existing methods.
- **0.0-0.2**: Routine application.
- *Note*: For reviews, novelty refers to the quality of synthesis and insight, not experimental novelty.

**3. Clarity (Weight: 30%)**: How well does it explain the field's landscape?
- **0.9-1.0**: Masterful synthesis that maps the field's structure, history, and logic. A newcomer could understand the big picture.
- **0.7-0.8**: Exceptionally clear. Explains not just "what" but "why" this problem matters to the field.
- **0.5-0.6**: Well-written. Core ideas are clear, but lacks broader context.
- **0.3-0.4**: Adequate but narrow. Assumes significant background knowledge.
- **0.0-0.2**: Poorly written or overly specialized.
- *Note*: Reviews should excel here and receive high scores (0.75-1.00) if they provide excellent field context.

**4. Potential (Weight: 30%)**: How well does it reveal future directions and open problems?
- **0.9-1.0**: Introduces multiple major discoveries or breakthroughs that could redefine the field.
- **0.7-0.8**: Clearly articulates multiple open challenges and future research directions for the field.
- **0.5-0.6**: Identifies key open problems or inspires new research directions.
- **0.3-0.4**: Points to incremental follow-up opportunities.
- **0.0-0.2**: Limited implications for future work.
- *Note*: Reviews that successfully map out future challenges should score very high (0.75-1.00).

**OUTPUT FORMAT (JSON):**
{{
  "significance_score": <float 0.0-1.0>,
  "novelty_score": <float 0.0-1.0>,
  "clarity_score": <float 0.0-1.0>,
  "potential_score": <float 0.0-1.0>,
  "justification": "<2-3 sentences. Explain how this paper helps us understand the field's priorities. For reviews, emphasize their value in synthesizing the landscape.>",
  "identified_problem": "<One precise phrase (5-10 words) describing the core problem or theme.>"
}}

**REMEMBER**: You're identifying the best "field guides," not the best research. A comprehensive review is often more valuable than a narrow technical breakthrough for our purpose."""),
            ("user", "Please analyze the following paper and rate how well it reveals the field's priorities and problems:{metadata_context}{temporal_instruction}\n\n---\n{paper_content}\n---")
        ])
        
        parser = JsonOutputParser()
        chain = prompt | self.llm | parser

        analysis_result = self._invoke_llm_with_fallback(
            chain, 
            paper_content,
            metadata_context=metadata_context,
            temporal_instruction=temporal_instruction
        )
        
        if "error" in analysis_result:
            return analysis_result
            
        required_keys = ["significance_score", "novelty_score", "clarity_score", "potential_score"]
        if not all(key in analysis_result for key in required_keys):
            return {"error": "LLM response was missing one or more required score keys."}

        return analysis_result

    def _summarize_hot_topics(self, synthesis_context: str) -> Dict[str, Any]:
        """
        (New) Synthesizes hot topics directly from a list of top-rated papers.
        This replaces the more complex map-reduce logic for simplicity and robustness.
        """
        print("    -> Synthesizing hot topics from top-rated papers...")

        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a senior research analyst. You have been given a list of top-rated papers from a specific field. Your task is to synthesize this information into a coherent overview of the field's hot topics.

The papers are provided below, each with a title, the core problem it addresses, and a justification for its high rating.
---
{synthesis_context}
---

Your final output MUST be a JSON object with the following structure:
{{
  "summary": "<A brief, coherent narrative (about 200-250 words) explaining what these hot topics are, how they relate to each other, and why they are important for the field. Integrate insights from the paper justifications, preserving any mentioned novel or unique points.>",
  "hot_topics": [
    {{
      "topic_name": "<The name of the first main hot topic, derived from the papers>",
      "challenge": "<A brief description of the core challenge or question for this topic.>",
      "related_papers": ["<Title of paper 1>", "<Title of paper 2>"]
    }}
  ]
}}

Instructions:
1.  Read through all the provided paper details.
2.  Identify 2-4 overarching themes or "hot topics" that emerge from the collective 'Identified Problem' fields.
3.  For each topic, formulate a concise `topic_name` and `challenge`.
4.  Group the paper titles under the most relevant `hot_topics` they belong to. A paper can be listed under multiple topics if it's relevant.
5.  For `related_papers`, you MUST use exact paper titles from the provided context only. Do NOT invent, rewrite, or normalize titles.
6.  Write the final `summary` narrative based on all the information.
"""),
            ("user", "The context containing the top-rated papers is provided above. Please generate the JSON output.")
        ])

        parser = JsonOutputParser()
        
        # 尝试使用 Gemini (如果配置了)
        synthesis_result = None
        if self.gemini_llm:
            try:
                print("    -> Attempting synthesis with Gemini...")
                chain = prompt | self.gemini_llm | parser
                synthesis_result = chain.invoke({
                    "synthesis_context": synthesis_context
                })
            except Exception as e:
                print(f"    ⚠️ Gemini synthesis failed (Timeout or Error): {e}")
                print("    -> Falling back to Main LLM (OpenAI)...")
                synthesis_result = None

        # 如果 Gemini 没配置或者失败了，使用主 LLM
        if not synthesis_result:
            try:
                chain = prompt | self.llm | parser
                synthesis_result = chain.invoke({
                    "synthesis_context": synthesis_context
                })
            except Exception as e:
                print(f"    🔴 Critical Error: Main LLM synthesis also failed: {e}")
                return {
                    "summary": "Synthesis failed.",
                    "hot_topics": []
                }

        return synthesis_result

    def _cluster_papers_by_llm(self, papers: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """
        (New) Uses an LLM to perform semantic clustering on a list of papers.
        """
        print("    -> High-score paper count exceeds threshold. Performing LLM-based semantic clustering...")

        paper_info = [
            {"title": p.get("title", "N/A"), "identified_problem": p.get("identified_problem", "N/A")}
            for p in papers
        ]

        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a senior research analyst. You have been given a list of papers, each with its title and the core problem it addresses. Your task is to group these papers into 3-5 high-level research themes based on the **semantic similarity** of their core problems.

Your task is **clustering, not summarization**.

The output MUST be a valid JSON object where:
- Each KEY is a concise, descriptive name for a research theme you identified (e.g., "On-Chip Quantum Light Sources").
- Each VALUE is a list of paper titles that belong to that theme.

Example Input:
[
  {{"title": "Paper A", "identified_problem": "scalable quantum entanglement"}},
  {{"title": "Paper B", "identified_problem": "generating multi-photon entangled states"}},
  {{"title": "Paper C", "identified_problem": "topological protection on photonic chips"}}
]

Example Output:
{{
  "Scalable Quantum Entanglement": ["Paper A", "Paper B"],
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
            return {"All High-Score Papers": [p["title"] for p in papers]}

    def run(self, professor_name: str, main_papers: List[Dict[str, Any]], ref1_papers: List[Dict[str, Any]] = None, cited_papers: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        执行工作流，分析所有论文并识别领域热点问题。
        """
        self._print_section_header("Workflow 2: Analyzing Field Problems", level=2)
        
        self.cache = CacheManager(professor_name, "field_problems_analysis")
        print(f"  -> Cache file set for professor '{professor_name}' in workflow 'field_problems_analysis'.")
        # 兼容空参
        if ref1_papers is None:
            ref1_papers = []
        if cited_papers is None:
            cited_papers = []

        # 新规则：该工作流可接收 main + ref1 + cited（由编排器按模式选择具体份额）
        all_papers = (main_papers or []) + ref1_papers + cited_papers
        
        if not all_papers:
            print("  -> No papers provided. Skipping workflow.")
            return {
                "summary": "没有提供任何论文，无法分析领域热点问题。",
                "hot_topics": [],
                "analyzed_papers": [],
            }

        # 1. 评估所有论文的“领域问题代表性”
        print(f"\n  [Step 1/2] Evaluating {len(all_papers)} papers for field relevance...")
        
        rated_papers = []
        
        with tqdm(total=len(all_papers), desc="  Rating papers") as pbar:
            for paper in all_papers:
                paper_id = paper["id"]
                
                cached_result = self.cache.get(paper_id)
                if cached_result:
                    pbar.update(1)
                    pbar.set_postfix_str("Cached")
                    if all(k in cached_result for k in ['significance_score', 'novelty_score', 'clarity_score', 'potential_score']):
                        # 将缓存结果与元数据合并
                        full_cached_result = {**cached_result, 'paper_id': paper_id, 'title': paper['title']}
                        
                        # 注入 DOI 和 INSPIRE URL
                        paper_metadata = paper.get('metadata')
                        if paper_metadata:
                            if paper_metadata.get('doi'):
                                full_cached_result['doi'] = paper_metadata['doi']
                            if paper_metadata.get('inspire_url'):
                                full_cached_result['inspire_url'] = paper_metadata['inspire_url']
                            full_cached_result['is_core_journal'] = bool(paper_metadata.get('is_core_journal', False))
                        else:
                            full_cached_result['is_core_journal'] = False
                        
                        rated_papers.append(full_cached_result)
                        continue
                    else:
                        pbar.set_postfix_str("Invalid Cache, Re-analyzing")

                paper_content = self._load_paper_content(paper["md_filename"])
                if not paper_content:
                    pbar.update(1)
                    pbar.set_postfix_str("Skipped (no content)")
                    continue

                # 提取论文元数据
                paper_metadata = paper.get('metadata')
                
                analysis_result = self._rate_single_paper(paper_content, paper_metadata)
                
                if "error" in analysis_result:
                    pbar.update(1)
                    pbar.set_postfix_str(f"Error ({analysis_result['error']})")
                    continue

                s_score = analysis_result.get('significance_score', 0)
                n_score = analysis_result.get('novelty_score', 0)
                c_score = analysis_result.get('clarity_score', 0)
                p_score = analysis_result.get('potential_score', 0)
                
                # 计算基础加权得分
                weighted_score = (s_score * 0.25) + (n_score * 0.1) + (c_score * 0.35) + (p_score * 0.3)
                
                # 应用时效性加权：更新的论文获得额外的权重提升
                recency_score = paper.get('recency_score', 0.5)
                if recency_score != 0.5:  # 只有有元数据的论文才应用此加权
                    # 时效性权重: 0.9-1.0的recency_score给予10%提升, 0.7-0.9给予5%提升
                    if recency_score >= 0.9:
                        weighted_score = weighted_score * 1.10
                    elif recency_score >= 0.7:
                        weighted_score = weighted_score * 1.05
                    # 非常旧的论文(recency_score < 0.3)稍微降权
                    elif recency_score < 0.3:
                        weighted_score = weighted_score * 0.95
                
                # 应用来源加权：核心代表作（primary）获得额外提升
                if paper.get('source_type') == 'primary':
                    weighted_score = weighted_score * 1.10  # 10% boost for primary papers
                
                analysis_result["weighted_score"] = round(weighted_score, 2)
                analysis_result["recency_score"] = recency_score  # 记录时效性得分

                # 注入 DOI 和 INSPIRE URL
                if paper_metadata:
                    if paper_metadata.get('doi'):
                        analysis_result['doi'] = paper_metadata['doi']
                    if paper_metadata.get('inspire_url'):
                        analysis_result['inspire_url'] = paper_metadata['inspire_url']
                    analysis_result['is_core_journal'] = bool(paper_metadata.get('is_core_journal', False))
                else:
                    analysis_result['is_core_journal'] = False

                full_result = {
                    **analysis_result, 
                    "paper_id": paper_id, 
                    "title": paper["title"],
                    "source_type": paper.get('source_type', 'primary')
                }
                
                # 注入 DOI 和 INSPIRE URL
                if paper_metadata:
                    if paper_metadata.get('doi'):
                        full_result['doi'] = paper_metadata['doi']
                    if paper_metadata.get('inspire_url'):
                        full_result['inspire_url'] = paper_metadata['inspire_url']
                    full_result['is_core_journal'] = bool(paper_metadata.get('is_core_journal', False))
                else:
                    full_result['is_core_journal'] = False
                
                rated_papers.append(full_result)
                self.cache.set(paper_id, analysis_result)
                
                pbar.update(1)
                pbar.set_postfix_str(f"Score: {weighted_score:.2f}")
                time.sleep(0.1)
        
        if not rated_papers:
            print("\n  -> No papers were successfully rated. Skipping synthesis.")
            return {
                "summary": "所有论文均未能成功评分，无法分析领域热点问题。",
                "hot_topics": [],
                "analyzed_papers": [],
            }

        # 2. 基于高分论文，综合分析热点问题
        print("\n  [Step 2/2] Synthesizing hot topics from top-rated papers...")
        
        high_score_threshold = 0.6
        high_score_papers = [p for p in rated_papers if p.get("weighted_score", 0.0) >= high_score_threshold]
        print(f"  -> Found {len(high_score_papers)} papers with score >= {high_score_threshold}.")

        # 优先使用核心期刊论文做热点综合；若没有核心期刊高分论文，则回退到全部高分论文
        core_high_score_papers = [p for p in high_score_papers if bool(p.get("is_core_journal", False))]
        if core_high_score_papers:
            synthesis_candidates = core_high_score_papers
            print(f"  -> Prioritizing core-journal papers for synthesis: {len(core_high_score_papers)} selected.")
        else:
            synthesis_candidates = high_score_papers
            print("  -> No core-journal papers in high-score set. Falling back to all high-score papers.")

        # 如果高质量论文过多，则进行聚类和代表性采样
        if len(synthesis_candidates) > 10:
            # 1. LLM语义聚类
            clusters = self._cluster_papers_by_llm(synthesis_candidates)
            
            # 2. 代表性提取
            representative_papers = []
            paper_map = {p["title"]: p for p in synthesis_candidates}
            
            for theme, titles in clusters.items():
                if not titles: continue
                
                # 找到该主题下分数最高的论文
                theme_papers = [paper_map[title] for title in titles if title in paper_map]
                if not theme_papers: continue
                
                best_paper_in_theme = max(theme_papers, key=lambda p: p.get("weighted_score", 0))
                representative_papers.append(best_paper_in_theme)
            
            # 去重，因为一篇论文可能属于多个聚类
            # 使用字典来去重，保持顺序
            final_papers_for_synthesis = list({p["paper_id"]: p for p in representative_papers}.values())
            print(f"  -> Clustered into {len(clusters)} themes. Selected {len(final_papers_for_synthesis)} representative papers for final synthesis.")
            top_papers = final_papers_for_synthesis
        else:
            # 如果论文数量不多，直接使用所有高分论文
            print("  -> Number of high-score papers is manageable. Using all for synthesis.")
            top_papers = synthesis_candidates

        if not top_papers:
            print("    ⚠️ No high-score papers found. Cannot synthesize hot topics.")
            return {
                "summary": "未能成功评估任何论文，无法生成领域热点问题总结。",
                "hot_topics": [],
                "analyzed_papers": []
            }

        synthesis_context = "Here are the top-rated papers identified as most representative of the field's key problems:\n\n"
        for i, paper in enumerate(top_papers, 1):
            synthesis_context += f"--- Paper {i} ---\n"
            synthesis_context += f"Title: {paper.get('title', 'N/A')}\n"
            synthesis_context += f"Identified Problem: {paper.get('identified_problem', 'N/A')}\n"
            synthesis_context += f"Justification: {paper.get('justification', 'N/A')}\n"
            synthesis_context += f"Weighted Score: {paper.get('weighted_score', 0):.2f}\n\n"

        summary_result = self._summarize_hot_topics(synthesis_context)

        return {
            "summary": summary_result.get("summary", "Could not generate summary."),
            "hot_topics": summary_result.get("hot_topics", []),
            "analyzed_papers": top_papers, # Return full objects
            "rated_papers": rated_papers # Return full objects including DOI/URL
        }
