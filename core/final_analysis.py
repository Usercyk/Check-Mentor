import json
from typing import Dict, Any, List
from . import config
from langchain_core.prompts import ChatPromptTemplate

class FinalAnalyzer:
    """
    负责将所有工作流的分析结果整合成一份最终的、连贯的报告。
    同时负责将报告翻译为指定语言。
    """
    def __init__(self, professor_name: str, llm=None, gemini_llm=None):
        """
        初始化最终分析器。

        Args:
            professor_name (str): 教授姓名。
            llm: 用于翻译的语言模型实例 (OpenAI)。
            gemini_llm: 用于翻译的 Gemini 模型实例 (优先使用)。
        """
        self.professor_name = professor_name
        self.llm = llm
        self.gemini_llm = gemini_llm

    def _get_with_warning(self, data: Dict, key: str, default: Any, source_name: str) -> Any:
        """
        尝试从字典中获取一个键。如果键不存在，则打印警告并返回默认值。
        """
        if key not in data:
            print(f"  -> ⚠️ WARNING: Key '{key}' not found in '{source_name}' results. Using default value.")
            return default
        return data.get(key, default)

    def translate_report(self, report_content: str, target_language: str = "Chinese") -> str:
        """
        将报告内容翻译成指定语言。
        """
        if not self.llm and not self.gemini_llm:
            print("  -> Translator LLM not provided. Skipping translation.")
            return report_content

        print(f"  -> Translating report to {target_language}...")
        
        prompt = ChatPromptTemplate.from_template(
            "You are a professional translator. Translate the following academic analysis report into {language}. "
            "Preserve the original Markdown formatting, including headers, lists, and bold text. "
            "Do NOT output any conversational filler (e.g., 'Here is the translation', 'Certainly'). "
            "Only output the translated report content directly.\n\n"
            "Report to translate:\n\n---\n{report}\n---"
        )
        
        translated_content = ""

        # 优先尝试 Gemini
        if self.gemini_llm:
            try:
                print("    -> Attempting translation with Gemini...")
                chain = prompt | self.gemini_llm
                translated_result = chain.invoke({
                    "language": target_language,
                    "report": report_content
                })
                print("    -> Gemini translation successful.")
                translated_content = translated_result.content
            except Exception as e:
                print(f"    ⚠️ Gemini translation failed: {e}")
                print("    -> Falling back to Main LLM (OpenAI)...")

        # 回退到主 LLM
        if not translated_content and self.llm:
            try:
                chain = prompt | self.llm
                translated_result = chain.invoke({
                    "language": target_language,
                    "report": report_content
                })
                print("  -> Translation successful.")
                translated_content = translated_result.content
            except Exception as e:
                print(f"  ⚠️ Error during translation: {e}. Returning original report.")
                return report_content
        
        if not translated_content:
            return report_content

        # Post-processing to remove potential AI filler
        # Split lines and remove leading lines that don't look like report content (e.g. "Sure!", "Here is...")
        # A simple heuristic: The report should start with a header "# "
        
        lines = translated_content.strip().split('\n')
        start_index = 0
        for i, line in enumerate(lines):
            if line.strip().startswith('# '):
                start_index = i
                break
        
        if start_index > 0:
            # If we found a header later, discard previous lines
            cleaned_content = '\n'.join(lines[start_index:])
        else:
            cleaned_content = translated_content

        return cleaned_content

    def generate_report_body(self, results: Dict[str, Any]) -> str:
        """
        生成报告的主体部分（前三章），这部分需要翻译。
        """
        # 从传入的 results 中提取各个部分
        contribution_analysis = results.get('contribution_analysis', {})
        field_problems_analysis = results.get('field_problems_analysis', {})
        undergrad_projects_analysis = results.get('undergrad_projects_analysis', {})

        # 准备报告的各个部分
        # 1. Title: Change to just professor name
        report_title = f"# {self.professor_name}\n\n"
        
        # 1. 核心贡献总结
        contribution_summary_str = "## 一、核心研究贡献\n\n"
        
        # 使用新的带警告的获取器
        research_directions = self._get_with_warning(contribution_analysis, 'research_directions', [], 'contribution_analysis')
        contribution_overview = self._get_with_warning(contribution_analysis, 'contribution_summary', '未能生成核心贡献总结。', 'contribution_analysis')

        if research_directions:
            contribution_summary_str += "### 研究方向\n"
            for i, direction in enumerate(research_directions, 1):
                contribution_summary_str += f"{direction}\n\n"
        
        contribution_summary_str += "### 贡献概述\n"
        contribution_summary_str += f"{contribution_overview}\n\n"



        # 2. 领域热点问题
        hot_topics_summary_str = "## 二、领域前沿与热点问题\n\n"
        field_summary = self._get_with_warning(field_problems_analysis, 'summary', '未能生成领域热点问题总结。', 'field_problems_analysis')
        hot_topics_summary_str += f"{field_summary}\n\n"
        
        # Build lookup map for links
        rated_papers = self._get_with_warning(field_problems_analysis, 'rated_papers', [], 'field_problems_analysis')
        paper_map = {}
        if rated_papers:
            for p in rated_papers:
                if isinstance(p, dict) and p.get('title'):
                    paper_map[p['title']] = p

        hot_topics = self._get_with_warning(field_problems_analysis, 'hot_topics', [], 'field_problems_analysis')
        if hot_topics:
            hot_topics_summary_str += "### 主要热点问题\n"
            for i, topic in enumerate(hot_topics, 1):
                hot_topics_summary_str += f"**{i}. {topic.get('topic_name', 'N/A')}**\n"
                hot_topics_summary_str += f"   - **核心挑战**: {topic.get('challenge', 'N/A')}\n"
                
                related_papers = topic.get('related_papers', [])
                papers_with_links = []
                for title in related_papers:
                    link = ""
                    if title in paper_map:
                        link = self._get_paper_link(paper_map[title])
                    papers_with_links.append(f"{title}{link}")
                
                hot_topics_summary_str += f"   - **相关论文**: {', '.join(papers_with_links)}\n\n"

        # 3. 本科生可参与项目
        undergrad_projects_summary_str = "## 三、本科生可参与的研究项目建议\n\n"
        undergrad_summary = self._get_with_warning(undergrad_projects_analysis, 'summary', '未能生成本科生项目建议。', 'undergrad_projects_analysis')
        undergrad_projects_summary_str += f"{undergrad_summary}\n\n"
        
        return report_title + contribution_summary_str + hot_topics_summary_str + undergrad_projects_summary_str

    def _get_paper_link(self, paper: Any) -> str:
        """Helper to extract link from paper object."""
        if not isinstance(paper, dict):
            return ""
        
        if paper.get('inspire_url'):
            return f" ({paper['inspire_url']})"
        elif paper.get('doi'):
            return f" (https://doi.org/{paper['doi']})"
        return ""

    def generate_report_appendix(self, results: Dict[str, Any]) -> str:
        """
        生成报告的附录部分（数据来源），这部分不需要翻译，保留原文（通常是英文论文标题）。
        """
        contribution_analysis = results.get('contribution_analysis', {})
        field_problems_analysis = results.get('field_problems_analysis', {})
        undergrad_projects_analysis = results.get('undergrad_projects_analysis', {})

        # 4. 数据来源附录
        appendix = "## 四、分析数据来源\n\n"
        appendix += "### 1. 教授核心贡献分析来源 (代表作)\n"
        analyzed_contrib_papers = self._get_with_warning(contribution_analysis, 'analyzed_papers', [], 'contribution_analysis')
        if analyzed_contrib_papers:
            # Limit to 6
            for paper in analyzed_contrib_papers[:6]:
                # Handle both string (title only) and dict (with 'title' key) formats
                link = self._get_paper_link(paper)
                if isinstance(paper, str):
                    appendix += f"- {paper}{link}\n"
                else:
                    appendix += f"- {paper.get('title', 'N/A')}{link}\n"
        else:
            appendix += "- 无\n"
        appendix += "\n"
        
        appendix += "### 2. 领域热点问题分析来源 (高分论文)\n"
        rated_field_papers_list = self._get_with_warning(field_problems_analysis, 'rated_papers', [], 'field_problems_analysis')
        # Filter for high-score papers (weighted_score >= 0.7)
        rated_field_papers = [p for p in rated_field_papers_list if p.get("weighted_score", 0) >= 0.7]
        
        if rated_field_papers:
            # Limit to 6
            for paper in rated_field_papers[:6]:
                # Handle both dict and string formats
                link = self._get_paper_link(paper)
                if isinstance(paper, dict):
                    appendix += f"- {paper.get('title', 'N/A')}{link}\n"
                else:
                    appendix += f"- {paper}{link}\n"
        else:
            appendix += "- 无\n"
        appendix += "\n"

        appendix += "### 3. 本科生项目建议来源 (复杂度与友好度筛选)\n"
        rated_undergrad_papers_list = self._get_with_warning(undergrad_projects_analysis, 'rated_papers', [], 'undergrad_projects_analysis')
        # Filter papers with moderate to high suitability (weighted_score >= 0.5)
        rated_undergrad_papers = [p for p in rated_undergrad_papers_list if p.get("score", 0) >= 0.5]
        
        if rated_undergrad_papers:
            # Limit to 6
            for paper in rated_undergrad_papers[:6]:
                link = self._get_paper_link(paper)
                appendix += f"- {paper.get('title', 'N/A')}{link}\n"
        else:
            appendix += "- 无\n"
        appendix += "\n"
        
        return appendix

    def generate_final_report(self, results: Dict[str, Any]) -> str:
        """
        生成最终的 Markdown 格式报告。

        Args:
            results (Dict[str, Any]): 来自 WorkflowOrchestrator 的完整结果。
        
        Returns:
            str: 格式化后的完整报告。
        """
        print("  -> Generating final report...")
        
        body = self.generate_report_body(results)
        appendix = self.generate_report_appendix(results)

        final_report = body + appendix
        
        print("  -> Final report generated successfully.")
        return final_report
