"""
学术数据爬虫模块的基础类和工具函数
"""
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class Paper:
    """论文数据结构"""
    title: str
    authors: List[str]
    year: Optional[int]
    abstract: Optional[str]
    url: Optional[str]
    citations: Optional[int]
    source: str  # 'scholar', 'arxiv', 'homepage'
    venue: Optional[str] = None  # 发表会议/期刊
    
    def __str__(self):
        return f"{self.title} ({self.year}) - {', '.join(self.authors[:3])}"


@dataclass
class ProfessorProfile:
    """导师学术档案"""
    name: str
    affiliation: Optional[str] = None
    homepage: Optional[str] = None
    email: Optional[str] = None
    research_interests: List[str] = None
    papers: List[Paper] = None
    
    def __post_init__(self):
        if self.research_interests is None:
            self.research_interests = []
        if self.papers is None:
            self.papers = []
