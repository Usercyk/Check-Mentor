"""
研究分析代理：使用 LLM 深度分析导师的研究方向和贡献
"""
from typing import List
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from agents import AgentState
import config


class ResearchAnalyzerAgent:
    """研究分析代理"""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model=config.LLM_MODEL,
            temperature=config.TEMPERATURE,
            api_key=config.OPENAI_API_KEY,
            base_url=config.OPENAI_API_BASE
        )
    
    def analyze_research(self, state: AgentState) -> AgentState:
        """
        分析导师的研究方向和贡献
        
        Args:
            state: 当前状态
            
        Returns:
            更新后的状态
        """
        print(f"\n{'='*60}")
        print(f"🔬 研究分析代理开始工作...")
        print(f"{'='*60}\n")
        
        papers = state["papers"]
        profile = state["profile"]
        
        if not papers:
            print("⚠️ 没有论文数据，跳过分析")
            return state
        
        # 准备论文摘要
        papers_summary = self._prepare_papers_summary(papers[:15])  # 只用前15篇
        
        # 1. 分析研究方向
        print("📍 分析研究方向...")
        research_directions = self._analyze_directions(papers_summary, profile)
        
        # 2. 分析关键贡献
        print("🏆 分析关键贡献...")
        key_contributions = self._analyze_contributions(papers_summary, profile)
        
        # 3. 分析领域核心问题
        print("🎯 分析领域核心问题...")
        field_problems = self._analyze_field_problems(
            research_directions, 
            papers_summary
        )
        
        # 更新状态
        state["research_directions"] = research_directions
        state["key_contributions"] = key_contributions
        state["field_problems"] = field_problems
        state["messages"].append(
            f"研究分析代理: 识别出 {len(research_directions)} 个研究方向"
        )
        
        return state
    
    def _prepare_papers_summary(self, papers: List) -> str:
        """准备论文摘要文本"""
        summary = []
        for i, paper in enumerate(papers, 1):
            summary.append(f"{i}. **{paper.title}** ({paper.year})")
            summary.append(f"   作者: {', '.join(paper.authors[:3])}")
            if paper.citations:
                summary.append(f"   引用: {paper.citations}")
            if paper.abstract:
                # 截取摘要前300字
                abstract_preview = paper.abstract[:300] + "..."
                summary.append(f"   摘要: {abstract_preview}")
            summary.append("")
        
        return "\n".join(summary)
    
    def _analyze_directions(self, papers_summary: str, profile) -> List[str]:
        """分析研究方向"""
        prompt = f"""
你是一位资深的物理学学术顾问。请基于以下导师的论文列表，总结其近期（最近3-5年）的主要研究方向。

导师信息:
- 姓名: {profile.name}
- 机构: {profile.affiliation or '未知'}
- 声明的研究兴趣: {', '.join(profile.research_interests) if profile.research_interests else '未知'}

近期论文:
{papers_summary}

请提供：
1. 3-5个主要研究方向（按重要性排序）
2. 每个方向用一句话简洁描述
3. 格式: "方向名称: 简短描述"

示例格式:
1. 拓扑量子材料: 研究新型拓扑绝缘体和拓扑超导体的电子结构
2. 量子输运现象: 探索低维系统中的量子输运特性

请直接给出研究方向列表，不要额外解释:
"""
        
        messages = [
            SystemMessage(content="你是一位资深物理学学术顾问，擅长分析研究方向。"),
            HumanMessage(content=prompt)
        ]
        
        response = self.llm.invoke(messages)
        
        # 解析响应
        directions = []
        for line in response.content.split('\n'):
            line = line.strip()
            if line and (line[0].isdigit() or line.startswith('-')):
                # 移除序号
                direction = line.lstrip('0123456789.-) ').strip()
                if direction:
                    directions.append(direction)
        
        print(f"  ✓ 识别出 {len(directions)} 个研究方向")
        for d in directions:
            print(f"    • {d}")
        
        return directions
    
    def _analyze_contributions(self, papers_summary: str, profile) -> str:
        """分析关键学术贡献"""
        prompt = f"""
基于以下论文列表，总结 {profile.name} 教授在各个研究方向上的代表性学术贡献。

论文列表:
{papers_summary}

请提供：
1. 识别高被引论文（如果有引用数据）
2. 总结每个主要方向的关键成果
3. 用本科生能理解的语言描述

要求：
- 简洁清晰，避免过多技术细节
- 突出创新点和影响力
- 300-500字

请直接给出分析结果:
"""
        
        messages = [
            SystemMessage(content="你是一位资深物理学学术顾问。"),
            HumanMessage(content=prompt)
        ]
        
        response = self.llm.invoke(messages)
        
        print(f"  ✓ 贡献分析完成 ({len(response.content)} 字)")
        
        return response.content
    
    def _analyze_field_problems(
        self, 
        research_directions: List[str], 
        papers_summary: str
    ) -> str:
        """分析领域核心问题"""
        prompt = f"""
基于以下研究方向和论文，分析这些领域当前的核心科学问题和技术挑战。

研究方向:
{chr(10).join([f"{i+1}. {d}" for i, d in enumerate(research_directions)])}

代表性论文:
{papers_summary}

请回答：
1. 这些研究方向正在解决什么宏观科学问题？
2. 当前面临的主要技术挑战是什么？
3. 这些研究的潜在应用价值是什么？

要求：
- 面向物理专业本科生，使用易懂的语言
- 突出研究的意义和前沿性
- 300-400字

请直接给出分析:
"""
        
        messages = [
            SystemMessage(content="你是一位物理学教授，擅长向本科生解释前沿研究。"),
            HumanMessage(content=prompt)
        ]
        
        response = self.llm.invoke(messages)
        
        print(f"  ✓ 领域问题分析完成")
        
        return response.content
