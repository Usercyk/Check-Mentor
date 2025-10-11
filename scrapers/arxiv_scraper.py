"""
arXiv 爬虫
使用 arxiv 库搜索预印本论文
"""
import arxiv
from typing import List
from datetime import datetime, timedelta

from scrapers import Paper
import config


class ArxivScraper:
    """arXiv 预印本论文爬虫"""
    
    def __init__(self):
        self.client = arxiv.Client()
    
    def search_papers(
        self, 
        author_name: str, 
        max_papers: int = None
    ) -> List[Paper]:
        """
        在 arXiv 上搜索作者的论文
        
        Args:
            author_name: 作者姓名
            max_papers: 最多获取的论文数量
            
        Returns:
            论文列表
        """
        if max_papers is None:
            max_papers = config.MAX_PAPERS_PER_SOURCE
        
        papers = []
        
        try:
            print(f"🔍 正在 arXiv 搜索: {author_name}")
            
            # 构建搜索查询
            search = arxiv.Search(
                query=f'au:"{author_name}"',
                max_results=max_papers * 2,
                sort_by=arxiv.SortCriterion.SubmittedDate
            )
            
            # 获取近期论文
            current_year = datetime.now().year
            cutoff_date = datetime.now() - timedelta(days=365 * config.RECENT_YEARS)
            
            for result in self.client.results(search):
                # 只保留近期论文
                if result.published >= cutoff_date:
                    paper = Paper(
                        title=result.title,
                        authors=[author.name for author in result.authors],
                        year=result.published.year,
                        abstract=result.summary,
                        url=result.entry_id,
                        citations=None,  # arXiv 不提供引用数
                        source='arxiv',
                        venue='arXiv preprint'
                    )
                    papers.append(paper)
                    print(f"  ✓ {paper.title[:60]}... ({paper.year})")
                
                if len(papers) >= max_papers:
                    break
            
            print(f"✅ 从 arXiv 获取到 {len(papers)} 篇论文")
            
        except Exception as e:
            print(f"❌ arXiv 搜索失败: {str(e)}")
        
        return papers
    
    def search_by_keywords(
        self, 
        keywords: List[str], 
        max_papers: int = 5
    ) -> List[Paper]:
        """
        根据关键词在 arXiv 上搜索相关论文（用于领域分析）
        
        Args:
            keywords: 关键词列表
            max_papers: 最多获取的论文数量
            
        Returns:
            论文列表
        """
        papers = []
        
        try:
            # 构建查询字符串
            query = ' AND '.join([f'all:"{kw}"' for kw in keywords])
            
            print(f"🔍 搜索关键词: {keywords}")
            
            search = arxiv.Search(
                query=query,
                max_results=max_papers,
                sort_by=arxiv.SortCriterion.Relevance
            )
            
            for result in self.client.results(search):
                paper = Paper(
                    title=result.title,
                    authors=[author.name for author in result.authors],
                    year=result.published.year,
                    abstract=result.summary,
                    url=result.entry_id,
                    citations=None,
                    source='arxiv',
                    venue='arXiv preprint'
                )
                papers.append(paper)
            
            print(f"✅ 找到 {len(papers)} 篇相关论文")
            
        except Exception as e:
            print(f"❌ 关键词搜索失败: {str(e)}")
        
        return papers
