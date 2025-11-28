"""
Workflow 3: 分析本科生可参与的项目

该工作流的目标是回答第三个核心问题：
"有哪些适合本科生参与的科研项目？"

它通过以下步骤实现：
1. 接收关键参考文献（ref1_papers）和潜在项目文献（cited_papers）作为输入。
2. 设计一个AI评估机制，从“工作复杂度”和“本科生友好度”两个维度对每篇论文进行打分。
3. 基于得分适中的论文，提炼出潜在的、可操作性强的本科生科研项目点。
"""
import json
import time
from typing import List, Dict, Any
from tqdm import tqdm

from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from .. import config
from .cache_manager import CacheManager

class UndergradProjectsWorkflow:
    """
    分析本科生可参与项目的工作流。
    """
    def __init__(self, main_llm, fallback_llm=None, gemini_llm=None, test_mode: bool = False):
        """
        初始化工作流，接收外部传入的LLM实例。
        """
        print("  -> UndergradProjectsWorkflow initialized.")
        self.llm = main_llm
        self.fallback_llm = fallback_llm
        self.gemini_llm = gemini_llm
        self.cache = None
        # 是否运行在测试模式（由编排器传入）
        self.test_mode = test_mode

    def _load_paper_content(self, file_path: str) -> str:
        """加载指定路径的 Markdown 文件内容。"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"    ⚠️ Error loading file {file_path}: {e}")
            return ""

    def _invoke_llm_with_fallback(self, chain, paper_content, contribution_summary, metadata_context=""):
        """
        调用LLM，如果主LLM失败，则尝试备用LLM。
        
        Args:
            chain: LangChain链
            paper_content: 论文内容
            contribution_summary: 教授贡献总结
            metadata_context: 元数据上下文信息
        """
        input_data = {
            "paper_content": paper_content[:12000],
            "contribution_summary": contribution_summary,
            "metadata_context": metadata_context
        }
        try:
            # print("      -> Attempting main LLM...")
            result = chain.invoke(input_data)
            return result
        except (OutputParserException, json.JSONDecodeError) as e:
            # print(f"      ⚠️ Main LLM output parsing failed: {e}. Retrying with main LLM...")
            try:
                result = chain.invoke(input_data)
                return result
            except Exception as final_e:
                # print(f"      ⚠️ Main LLM retry failed: {final_e}.")
                pass
        except Exception as e:
            # print(f"      ⚠️ Main LLM failed: {e}")
            pass

        if self.fallback_llm:
            try:
                # print("      -> Attempting fallback LLM...")
                fallback_chain = chain.with_components(llm=self.fallback_llm)
                result = fallback_chain.invoke(input_data)
                return result
            except Exception as e:
                # print(f"      ⚠️ Fallback LLM also failed: {e}")
                pass
        
        return {"error": "Both main and fallback LLMs failed."}

    def _evaluate_single_paper(self, paper_content: str, contribution_summary: str, metadata: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        使用 LLM 评估单篇论文，基于四维模型进行打分。
        
        Args:
            paper_content: 论文内容
            contribution_summary: 教授贡献总结
            metadata: 论文元数据（可选）
        """
        # 构建元数据上下文
        metadata_context = ""
        recency_note = ""
        
        if metadata:
            metadata_context = "\n\n**Paper Metadata:**"
            if metadata.get("publish_date"):
                metadata_context += f"\n- Publication Date: {metadata['publish_date']}"
                
                # 根据发布时间添加说明
                try:
                    from datetime import datetime
                    pub_year = int(metadata['publish_date'][:4])
                    current_year = datetime.now().year
                    age = current_year - pub_year
                    
                    if age <= 2:
                        recency_note = "\n\n**RECENCY NOTE**: This is a very recent paper. Recent papers may use cutting-edge techniques that are more relevant to current research trends, but they might also require more specialized knowledge. Consider both the potential for learning modern techniques and the accessibility for undergraduates."
                    elif age >= 8:
                        recency_note = "\n\n**RECENCY NOTE**: This is an older paper. While foundational concepts remain valuable, consider whether the techniques or approaches are still current in the field. Older papers may be more accessible (using well-established methods) but might not reflect modern research directions."
                except:
                    pass
            
            if metadata.get("authors"):
                metadata_context += f"\n- Authors: {', '.join(metadata['authors'][:3])}"
                if len(metadata['authors']) > 3:
                    metadata_context += f" (and {len(metadata['authors']) - 3} more)"
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an experienced professor evaluating papers for potential undergraduate research projects. Your goal is to find projects that are not only feasible but also relevant to your own research interests and valuable for a student's growth.

You will be given a summary of your own core research contributions and the content of a candidate paper. You must evaluate the paper based on the following four criteria. Each score MUST be a float between 0.0 and 1.0.

**Your Core Research Summary:**
---
{contribution_summary}
---

**Evaluation Criteria:**

1.  **Topical Relevance (Weight: 40%)**: How closely does this paper's topic align with YOUR core research summary?
    - 1.0: Directly related to a key theme in your summary.
    - 0.5: Tangentially related, or on a neighboring topic.
    - 0.0: Completely unrelated.

2.  **Technical Accessibility (Weight: 25%)**: How feasible is it for an undergraduate to engage with the technical aspects?
    - 1.0: Relies on standard undergraduate-level knowledge and common tools.
    - 0.5: Requires some specialized knowledge, but it's learnable within a semester.
    - 0.0: Requires deep, graduate-level expertise.

3.  **Project Modularity (Weight: 20%)**: Can a well-defined, self-contained sub-project be carved out from this paper?
    - 1.0: The paper's methods or components are clearly separable into smaller tasks (e.g., "reproduce figure 2," "implement algorithm X").
    - 0.5: A sub-project is possible but requires careful definition by the mentor.
    - 0.0: The work is monolithic and cannot be broken down.

4.  **Educational Value (Weight: 15%)**: How much would a student learn by doing a project from this paper?
    - 1.0: The project would teach fundamental skills and provide a "big picture" view of the field.
    - 0.5: The project is a good learning experience for a specific skill.
    - 0.0: The work is tedious, repetitive, or too narrow to be educationally valuable.

Your final output MUST be a JSON object with the following structure:
{{
  "relevance_score": <float>,
  "accessibility_score": <float>,
  "modularity_score": <float>,
  "educational_score": <float>,
  "justification": "<A brief justification for your scores, referencing the four criteria.>",
  "project_idea": "<A concrete, one-sentence project idea for an undergraduate. If not suitable, state 'Not suitable'.>"
}}

IMPORTANT: Output ONLY the JSON object above. Do NOT include any extra text, code fences, or explanations before or after the JSON."""),
            ("user", "Please evaluate the following paper content for undergraduate project suitability and provide the structured JSON output:{metadata_context}{recency_note}\n\n**Paper Content:**\n---\n{paper_content}\n---")
        ])
        
        parser = JsonOutputParser()

        # 为提升 JSON 稳定性：此步强制使用较低温度；若不支持 bind，则回退为原模型
        try:
            llm_low_temp = self.llm.bind(temperature=0.0)
        except Exception:
            llm_low_temp = self.llm

        def _call_and_parse_with_clean(llm_to_use):
            chain_text = prompt | llm_to_use
            result_obj = chain_text.invoke({
                "paper_content": paper_content[:12000],
                "contribution_summary": contribution_summary,
                "metadata_context": metadata_context,
                "recency_note": recency_note
            })
            raw_text = getattr(result_obj, "content", result_obj)
            # 尝试严格解析
            try:
                return parser.parse(raw_text)
            except Exception:
                # 宽松清洗：移除可能的代码围栏，截取第一个 '{' 到最后一个 '}'
                try:
                    import re, json as _json
                    cleaned = re.sub(r"```[a-zA-Z]*", "", str(raw_text))
                    start = cleaned.find("{")
                    end = cleaned.rfind("}")
                    if start != -1 and end != -1 and end > start:
                        candidate = cleaned[start:end+1]
                        data = _json.loads(candidate)
                        return data
                except Exception:
                    pass
                return {"error": "LLM output could not be parsed as JSON."}

        # 先试主模型
        parsed = _call_and_parse_with_clean(llm_low_temp)
        if not isinstance(parsed, dict) or parsed.get("error"):
            # 再试备用模型
            if self.fallback_llm:
                try:
                    try:
                        fallback_low = self.fallback_llm.bind(temperature=0.0)
                    except Exception:
                        fallback_low = self.fallback_llm
                    parsed_fb = _call_and_parse_with_clean(fallback_low)
                    return parsed_fb
                except Exception:
                    pass
            return {"error": "Both main and fallback LLMs failed."}
        return parsed

    def _cluster_papers_by_llm(self, papers: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """
        使用LLM对论文进行语义聚类。
        """
        print("    -> High-quality paper count exceeds threshold. Performing LLM-based semantic clustering...")

        paper_info = [
            {"title": p.get("title", "N/A"), "project_idea": p.get("project_idea", "N/A")}
            for p in papers
        ]

        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a senior research analyst. You have been given a list of papers, each with its title and a proposed undergraduate project idea. Your task is to group these papers into 3-5 high-level project themes based on the **semantic similarity** of their project ideas.

Your task is **clustering, not summarization**.

The output MUST be a valid JSON object where:
- Each KEY is a concise, descriptive name for a project theme you identified (e.g., "Quantum Device Simulation", "Optical System Design").
- Each VALUE is a list of paper titles that belong to that theme.

Example Input:
[
  {{"title": "Paper A", "project_idea": "simulate quantum entanglement on a chip"}},
  {{"title": "Paper B", "project_idea": "design multi-photon source"}},
  {{"title": "Paper C", "project_idea": "build topological waveguide simulator"}}
]

Example Output:
{{
  "Quantum Simulation Projects": ["Paper A"],
  "Photonic Device Design": ["Paper B", "Paper C"]
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
            return {"All Suitable Papers": [p["title"] for p in papers]}

    def _synthesize_project_suggestions(self, suitable_papers: List[Dict[str, Any]]) -> str:
        """
        基于筛选出的论文，综合生成一份项目建议总结。
        如果论文过多，会进行聚类和代表性采样。
        """
        # 如果合适的论文过多，进行聚类和代表性采样
        papers_for_synthesis = suitable_papers
        
        if len(suitable_papers) > 10:
            print(f"    -> Found {len(suitable_papers)} suitable papers. Performing clustering and representative sampling...")
            
            # 1. LLM语义聚类
            clusters = self._cluster_papers_by_llm(suitable_papers)
            
            # 2. 代表性提取：从每个主题中选择加权得分最高的论文
            representative_papers = []
            paper_map = {p["title"]: p for p in suitable_papers}
            
            for theme, titles in clusters.items():
                if not titles: continue
                
                # 找到该主题下加权得分最高的论文
                theme_papers = [paper_map[title] for title in titles if title in paper_map]
                if not theme_papers: continue
                
                best_paper_in_theme = max(theme_papers, key=lambda p: p.get("weighted_score", 0))
                representative_papers.append(best_paper_in_theme)
            
            # 去重
            papers_for_synthesis = list({p["paper_id"]: p for p in representative_papers}.values())
            print(f"    -> Clustered into {len(clusters)} themes. Selected {len(papers_for_synthesis)} representative papers for synthesis.")
        else:
            print(f"    -> Number of suitable papers ({len(suitable_papers)}) is manageable. Using all for synthesis.")
        
        prompt = ChatPromptTemplate.from_template("""You are a helpful academic advisor. Based on a list of papers suitable for undergraduates, create a summary of potential research project areas.

The evaluated papers are provided below:
{papers_json}

Your summary should:
1. Group the project ideas into 2-3 thematic areas.
2. Provide a brief, encouraging narrative about why these areas are exciting for undergraduate research.
3. Be about 150-200 words.

Synthesized Summary of Project Suggestions:""")

        papers_json_str = json.dumps(papers_for_synthesis, indent=2, ensure_ascii=False)

        # 尝试使用 Gemini (如果配置了)
        result = None
        if self.gemini_llm:
            try:
                print("    -> Attempting synthesis with Gemini...")
                chain = prompt | self.gemini_llm
                result = chain.invoke({"papers_json": papers_json_str})
            except Exception as e:
                print(f"    ⚠️ Gemini synthesis failed (Timeout or Error): {e}")
                print("    -> Falling back to Main LLM (OpenAI)...")
                result = None

        # 如果 Gemini 没配置或者失败了，使用主 LLM
        if not result:
            try:
                chain = prompt | self.llm
                result = chain.invoke({"papers_json": papers_json_str})
            except Exception as e:
                print(f"    🔴 Critical Error: Main LLM synthesis also failed: {e}")
                return "Failed to synthesize project suggestions."

        return result.content if hasattr(result, 'content') else str(result)

    def run(self, professor_name: str, main_papers: List[Dict[str, Any]], cited_papers: List[Dict[str, Any]], contribution_summary: str) -> Dict[str, Any]:
        """
        执行分析本科生项目的完整流程。
        """
        self.cache = CacheManager(professor_name, "undergrad_projects_analysis")
        # 新规则：该工作流可接收 main + cited（由编排器按模式选择具体份额）
        all_papers = (main_papers or []) + (cited_papers or [])
        print(f"  -> Running UndergradProjectsWorkflow on {len(all_papers)} papers (main + cited).")

        if not all_papers:
            print("  -> No papers provided. Skipping workflow.")
            return {
                "summary": "没有提供任何论文，无法分析本科生可参与的项目。",
                "project_ideas": [],
                "rated_papers": []
            }
        
        if not contribution_summary:
            print("    ⚠️ Warning: Professor's contribution summary is empty. Topical relevance score may be inaccurate.")


        # 步骤1: 对每篇论文进行评估
        all_evaluated_papers = []
        for paper in tqdm(all_papers, desc="  -> Evaluating undergrad projects"):
            paper_id = paper['id']
            cached_result = self.cache.get(
                paper_id,
                required_keys=[
                    "paper_id", "title", "project_idea", "justification",
                    "relevance_score", "accessibility_score", "modularity_score", "educational_score",
                    "weighted_score"
                ]
            )

            if cached_result:
                evaluation = cached_result
                # 确保缓存结果也包含时效性得分
                if 'recency_score' not in evaluation and 'recency_score' in paper:
                    evaluation['recency_score'] = paper['recency_score']
            else:
                content = self._load_paper_content(paper['md_filename'])
                if not content:
                    continue
                
                # 提取元数据
                paper_metadata = paper.get('metadata')
                
                evaluation_result = self._evaluate_single_paper(content, contribution_summary, paper_metadata)

                # LLM 评估失败时的处理：
                # - 测试模式：使用保守的启发式回退结果，避免整条工作流中断
                # - 非测试模式：沿用原逻辑，跳过该论文
                if evaluation_result.get("error"):
                    if self.test_mode:
                        tqdm.write(f"    ⚠️ LLM failed for '{paper['title']}'. Using fallback heuristic in test mode.")
                        # 简单启发式：给出温和、偏保守的分数，确保后续流程可继续
                        # 如果存在时效性信息，稍微影响分数
                        recency_score = paper.get('recency_score', 0.5)
                        # 基础分（0.0~1.0区间内的温和取值）
                        base_relevance = 0.4
                        base_accessibility = 0.55
                        base_modularity = 0.5
                        base_educational = 0.55
                        # 根据时效性微调（较新的论文略降可达性，较旧的论文略降相关性）
                        if recency_score >= 0.85:
                            base_accessibility = max(0.45, base_accessibility - 0.08)
                        elif recency_score <= 0.35:
                            base_relevance = max(0.3, base_relevance - 0.08)

                        evaluation_result = {
                            "relevance_score": round(base_relevance, 3),
                            "accessibility_score": round(base_accessibility, 3),
                            "modularity_score": round(base_modularity, 3),
                            "educational_score": round(base_educational, 3),
                            "justification": "Fallback heuristic due to LLM failure in test mode: assigned conservative mid-low scores to continue the pipeline.",
                            "project_idea": "Not suitable"
                        }
                    else:
                        tqdm.write(f"    ⚠️ Skipped paper '{paper['title']}' due to LLM failure.")
                        continue

                # 计算加权分数
                r_score = evaluation_result.get("relevance_score", 0.0)
                a_score = evaluation_result.get("accessibility_score", 0.0)
                m_score = evaluation_result.get("modularity_score", 0.0)
                e_score = evaluation_result.get("educational_score", 0.0)

                weighted_score = (r_score * 0.4) + (a_score * 0.25) + (m_score * 0.2) + (e_score * 0.15)
                
                # 应用时效性权重：对于本科生项目，适度新的论文更合适
                # 太新可能太难，太旧可能过时
                recency_score = paper.get('recency_score', 0.5)
                if recency_score != 0.5:
                    # 对于本科生项目：
                    # - 非常新的论文(>0.9)可能过于前沿，不加权或轻微降权
                    # - 适度新的论文(0.6-0.9)最适合，给予提升
                    # - 较旧的论文(<0.4)可能过时，轻微降权
                    if 0.6 <= recency_score <= 0.9:
                        weighted_score = weighted_score * 1.08  # 8%提升
                    elif recency_score > 0.9:
                        weighted_score = weighted_score * 0.98  # 2%降权（太新可能太难）
                    elif recency_score < 0.4:
                        weighted_score = weighted_score * 0.95  # 5%降权

                # 构建完整的评估对象并缓存
                evaluation = {
                    **evaluation_result,
                    'paper_id': paper_id,
                    'title': paper['title'],
                    'weighted_score': round(weighted_score, 4),
                    'recency_score': recency_score
                }
                self.cache.set(paper_id, evaluation)
                time.sleep(1) # Delay after successful API call

            all_evaluated_papers.append(evaluation)

        if not all_evaluated_papers:
            print("\n  -> No papers were successfully evaluated. Skipping synthesis.")
            return {
                "summary": "所有论文均未能成功评估，无法分析本科生可参与的项目。",
                "project_ideas": [],
                "rated_papers": []
            }

        # 步骤2: 筛选合适的论文
        high_score_threshold = 0.5 # Adjusted threshold for the new weighted score
        suitable_papers = [
            p for p in all_evaluated_papers 
            if p.get("weighted_score", 0.0) >= high_score_threshold
        ]
        print(f"\n    -> Found {len(suitable_papers)} suitable papers for undergraduate projects.")

        # 步骤3: 综合项目建议
        if suitable_papers:
            print("    -> Synthesizing project suggestions...")
            summary = self._synthesize_project_suggestions(suitable_papers)
            project_ideas = [
                {
                    "paper_id": p['paper_id'],
                    "title": p['title'],
                    "idea": p.get("project_idea")
                }
                for p in suitable_papers if "Not suitable" not in p.get("project_idea", "")
            ]
        else:
            print("    -> No suitable papers found. Cannot synthesize project suggestions.")
            summary = "没有发现与教授研究方向相关、且适合本科生参与的论文，无法提供具体的项目建议。"
            project_ideas = []

        # 步骤4: 格式化最终输出
        final_result = {
            "summary": summary,
            "project_ideas": project_ideas,
            "rated_papers": [
                {
                    "paper_id": p['paper_id'],
                    "title": p['title'],
                    "score": p.get('weighted_score', 'N/A'),
                    "details": {
                        "relevance": p.get('relevance_score', 'N/A'),
                        "accessibility": p.get('accessibility_score', 'N/A'),
                        "modularity": p.get('modularity_score', 'N/A'),
                        "education": p.get('educational_score', 'N/A')
                    },
                    "justification": p.get('justification', 'N/A')
                }
                for p in all_evaluated_papers
            ]
        }

        return final_result
