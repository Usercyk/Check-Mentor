"""
数据收集代理：负责收集导师的学术信息
"""
from typing import List
from langchain_core.messages import HumanMessage, SystemMessage

from agents import AgentState
from scrapers import Paper, ProfessorProfile
from scrapers.scholar_scraper import ScholarScraper
from scrapers.arxiv_scraper import ArxivScraper


class DataCollectorAgent:
    """数据收集代理"""
    
    def __init__(self):
        self.scholar_scraper = ScholarScraper()
        self.arxiv_scraper = ArxivScraper()
    
    def collect_data(self, state: AgentState) -> AgentState:
        """
        收集导师的学术数据
        
        Args:
            state: 当前状态
            
        Returns:
            更新后的状态
        """
        professor_name = state["professor_name"]
        
        print(f"\n{'='*60}")
        print(f"📊 数据收集代理开始工作...")
        print(f"{'='*60}\n")
        
        # 1. 从 Google Scholar 获取基本信息和论文
        profile = self.scholar_scraper.search_professor(professor_name)
        scholar_papers = self.scholar_scraper.get_recent_papers(professor_name)
        
        # 2. 从 arXiv 获取预印本论文
        arxiv_papers = self.arxiv_scraper.search_papers(professor_name)
        
        # 3. 合并论文列表（去重）
        all_papers = scholar_papers + arxiv_papers
        unique_papers = self._deduplicate_papers(all_papers)
        
        # 按年份和引用数排序
        unique_papers.sort(
            key=lambda p: (p.year or 0, p.citations or 0), 
            reverse=True
        )
        
        print(f"\n📈 数据收集完成:")
        print(f"  - 导师信息: {profile.name if profile else '未找到'}")
        print(f"  - 论文总数: {len(unique_papers)}")
        print(f"  - Google Scholar: {len(scholar_papers)}")
        print(f"  - arXiv: {len(arxiv_papers)}")
        
        # 更新状态
        state["profile"] = profile or ProfessorProfile(name=professor_name)
        state["papers"] = unique_papers
        state["messages"].append(
            f"数据收集代理: 成功收集 {len(unique_papers)} 篇论文"
        )
        
        return state
    
    def _deduplicate_papers(self, papers: List[Paper]) -> List[Paper]:
        """去除重复的论文"""
        seen_titles = set()
        unique_papers = []
        
        for paper in papers:
            # 简单的标题相似度判断（转小写、去空格）
            normalized_title = paper.title.lower().replace(" ", "")
            
            if normalized_title not in seen_titles:
                seen_titles.add(normalized_title)
                unique_papers.append(paper)
        
        return unique_papers
