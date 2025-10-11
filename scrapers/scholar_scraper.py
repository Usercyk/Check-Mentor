"""
Google Scholar 爬虫
使用 scholarly 库获取导师的学术信息
"""
import time
from typing import List, Optional
from scholarly import scholarly, ProxyGenerator
from tenacity import retry, stop_after_attempt, wait_exponential

from scrapers import Paper, ProfessorProfile
import config


class ScholarScraper:
    """Google Scholar 数据爬虫"""
    
    def __init__(self):
        """初始化爬虫"""
        # 可选：设置代理以避免被封禁
        # pg = ProxyGenerator()
        # scholarly.use_proxy(pg)
        pass
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=10))
    def search_professor(self, professor_name: str) -> Optional[ProfessorProfile]:
        """
        搜索教授的 Google Scholar 主页
        
        Args:
            professor_name: 教授姓名
            
        Returns:
            ProfessorProfile 对象，如果未找到则返回 None
        """
        try:
            print(f"🔍 正在 Google Scholar 搜索: {professor_name}")
            
            # 搜索作者
            search_query = scholarly.search_author(professor_name)
            author = next(search_query, None)
            
            if not author:
                print(f"❌ 未找到 {professor_name} 的 Scholar 主页")
                return None
            
            # 获取详细信息
            author_detail = scholarly.fill(author)
            
            profile = ProfessorProfile(
                name=author_detail.get('name', professor_name),
                affiliation=author_detail.get('affiliation', None),
                homepage=author_detail.get('homepage', None),
                email=author_detail.get('email', None),
                research_interests=author_detail.get('interests', [])
            )
            
            print(f"✅ 找到导师: {profile.name} - {profile.affiliation}")
            return profile
            
        except Exception as e:
            print(f"⚠️ Google Scholar 搜索出错: {str(e)}")
            return None
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=10))
    def get_recent_papers(
        self, 
        professor_name: str, 
        max_papers: int = None
    ) -> List[Paper]:
        """
        获取教授的近期论文
        
        Args:
            professor_name: 教授姓名
            max_papers: 最多获取的论文数量
            
        Returns:
            论文列表
        """
        if max_papers is None:
            max_papers = config.MAX_PAPERS_PER_SOURCE
        
        papers = []
        
        try:
            # 搜索作者
            search_query = scholarly.search_author(professor_name)
            author = next(search_query, None)
            
            if not author:
                return papers
            
            # 获取详细信息
            author_detail = scholarly.fill(author)
            
            # 获取论文列表
            publications = author_detail.get('publications', [])
            current_year = 2025
            cutoff_year = current_year - config.RECENT_YEARS
            
            print(f"📚 正在获取 {professor_name} 的近期论文...")
            
            for pub in publications[:max_papers * 2]:  # 多获取一些以便筛选
                try:
                    # 填充论文详情
                    pub_detail = scholarly.fill(pub)
                    
                    # 提取年份
                    year_str = pub_detail.get('bib', {}).get('pub_year', None)
                    year = int(year_str) if year_str else None
                    
                    # 只保留近期论文
                    if year and year >= cutoff_year:
                        paper = Paper(
                            title=pub_detail.get('bib', {}).get('title', 'Unknown'),
                            authors=pub_detail.get('bib', {}).get('author', '').split(' and '),
                            year=year,
                            abstract=pub_detail.get('bib', {}).get('abstract', None),
                            url=pub_detail.get('pub_url', None),
                            citations=pub_detail.get('num_citations', 0),
                            source='scholar',
                            venue=pub_detail.get('bib', {}).get('venue', None)
                        )
                        papers.append(paper)
                        print(f"  ✓ {paper.title[:60]}... ({year})")
                    
                    if len(papers) >= max_papers:
                        break
                    
                    # 避免请求过快
                    time.sleep(1)
                    
                except Exception as e:
                    print(f"  ⚠️ 跳过一篇论文: {str(e)}")
                    continue
            
            print(f"✅ 获取到 {len(papers)} 篇近期论文")
            
        except Exception as e:
            print(f"❌ 获取论文列表失败: {str(e)}")
        
        return papers
