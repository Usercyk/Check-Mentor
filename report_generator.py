"""
报告生成器：将分析结果转换为 Markdown 格式的报告
"""
from datetime import datetime
from typing import List
from pathlib import Path

from scrapers import Paper, ProfessorProfile
import config


class ReportGenerator:
    """学术报告生成器"""
    
    def generate_report(
        self,
        profile: ProfessorProfile,
        papers: List[Paper],
        research_directions: List[str],
        key_contributions: str,
        field_problems: str,
        beginner_tasks: List[str]
    ) -> str:
        """
        生成完整的 Markdown 报告
        
        Args:
            profile: 导师档案
            papers: 论文列表
            research_directions: 研究方向
            key_contributions: 关键贡献
            field_problems: 领域问题
            beginner_tasks: 本科生任务
            
        Returns:
            Markdown 格式的报告
        """
        sections = []
        
        # 标题
        sections.append(f"# 🎓 {profile.name} 教授学术档案")
        sections.append(f"*为物理学本科生准备的科研指南*\n")
        sections.append(f"---\n")
        
        # 基本信息
        sections.append("## 📋 基本信息\n")
        sections.append(f"- **姓名**: {profile.name}")
        if profile.affiliation:
            sections.append(f"- **所属机构**: {profile.affiliation}")
        if profile.homepage:
            sections.append(f"- **个人主页**: [{profile.homepage}]({profile.homepage})")
        if profile.research_interests:
            sections.append(f"- **研究兴趣**: {', '.join(profile.research_interests)}")
        sections.append(f"- **分析论文数**: {len(papers)} 篇")
        sections.append(f"- **报告生成时间**: {datetime.now().strftime('%Y年%m月%d日')}\n")
        sections.append("---\n")
        
        # 第一部分：研究方向
        sections.append("## 🔬 一、近期研究方向\n")
        sections.append("*基于最近3-5年的论文分析*\n")
        for i, direction in enumerate(research_directions, 1):
            sections.append(f"### {i}. {direction}\n")
        sections.append("---\n")
        
        # 第二部分：代表性贡献
        sections.append("## 🏆 二、代表性学术贡献\n")
        sections.append(key_contributions)
        sections.append("\n---\n")
        
        # 第三部分：领域核心问题
        sections.append("## 🎯 三、领域核心问题与挑战\n")
        sections.append("*学术界正在关注什么？*\n")
        sections.append(field_problems)
        sections.append("\n---\n")
        
        # 第四部分：本科生科研任务
        sections.append("## 🚀 四、本科生科研入门建议\n")
        sections.append("*循序渐进的科研任务设计*\n")
        for i, task in enumerate(beginner_tasks, 1):
            sections.append(f"### 任务 {i}\n")
            sections.append(task)
            sections.append("\n")
        sections.append("---\n")
        
        # 第五部分：重要论文列表
        sections.append("## 📚 五、重要论文列表\n")
        sections.append("*近期高质量论文*\n")
        
        # 选择前10篇论文（按引用数和年份）
        top_papers = sorted(
            papers[:20], 
            key=lambda p: (p.citations or 0, p.year or 0), 
            reverse=True
        )[:10]
        
        for i, paper in enumerate(top_papers, 1):
            sections.append(f"### {i}. {paper.title}\n")
            sections.append(f"- **作者**: {', '.join(paper.authors[:5])}")
            if len(paper.authors) > 5:
                sections.append(" et al.")
            sections.append(f"\n- **年份**: {paper.year}")
            if paper.citations:
                sections.append(f"\n- **引用数**: {paper.citations}")
            if paper.venue:
                sections.append(f"\n- **发表于**: {paper.venue}")
            if paper.url:
                sections.append(f"\n- **链接**: [{paper.url}]({paper.url})")
            sections.append("\n")
        
        sections.append("---\n")
        
        # 结语
        sections.append("## 💬 结语\n")
        sections.append(
            "本报告由 AI 自动生成，旨在帮助本科生快速了解导师的研究方向和可能的科研切入点。"
            "建议在阅读本报告后，结合导师的个人主页和代表性论文，形成自己的理解。"
            "最重要的是，带着具体的问题和想法，与导师进行面对面的交流。\n"
        )
        sections.append("**祝你的科研之旅一帆风顺！🌟**\n")
        
        return "\n".join(sections)
    
    def save_report(self, report: str, professor_name: str) -> Path:
        """
        保存报告到文件
        
        Args:
            report: 报告内容
            professor_name: 教授姓名
            
        Returns:
            报告文件路径
        """
        # 生成文件名
        filename = f"{professor_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.md"
        filepath = config.REPORTS_DIR / filename
        
        # 保存文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"\n✅ 报告已保存: {filepath}")
        
        return filepath
