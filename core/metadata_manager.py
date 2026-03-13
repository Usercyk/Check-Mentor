"""
论文元数据管理模块

该模块负责处理论文的元数据，包括：
- DOI (论文唯一标识符)
- 作者列表
- 发布时间

元数据的应用包括：
- 按发布时间对论文进行排序和加权
- 提供更准确的论文信息
"""
import json
import re
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path


class PaperMetadata:
    """论文元数据类"""
    
    def __init__(
        self,
        doi: str = "",
        inspire_url: Optional[str] = None,
        authors: List[str] = None,
        publish_year: Optional[int] = None,
        publish_month: Optional[int] = None
    ):
        """
        初始化论文元数据
        
        Args:
            doi: 论文的DOI标识符
            inspire_url: INSPIRE数据库链接
            authors: 作者列表
            publish_year: 发布年份
            publish_month: 发布月份
        """
        self.doi = doi
        self.inspire_url = inspire_url
        self.authors = authors if authors is not None else []
        self.publish_year = publish_year
        self.publish_month = publish_month
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式（向后兼容）"""
        result = {
            "doi": self.doi,
            "inspire_url": self.inspire_url,
            "authors": self.authors,
        }
        
        # 新格式：published 字典
        if self.publish_year is not None:
            result["published"] = {"year": self.publish_year}
            if self.publish_month is not None:
                result["published"]["month"] = self.publish_month
        
        # 向后兼容：添加 publish_date 字符串（用于现有的工作流代码）
        if self.publish_year is not None:
            if self.publish_month is not None:
                # 如果有月份，生成 YYYY-MM 格式
                result["publish_date"] = f"{self.publish_year}-{self.publish_month:02d}"
            else:
                # 如果只有年份，生成 YYYY 格式
                result["publish_date"] = str(self.publish_year)
        
        return result
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PaperMetadata':
        """从字典创建元数据对象"""
        publish_year = None
        publish_month = None
        
        # 处理新格式：published 字典
        if "published" in data and isinstance(data["published"], dict):
            publish_year = data["published"].get("year")
            publish_month = data["published"].get("month")
        # 兼容旧格式：publish_date 字符串
        elif "publish_date" in data and isinstance(data["publish_date"], str):
            try:
                date = datetime.fromisoformat(data["publish_date"])
                publish_year = date.year
                publish_month = date.month
            except (ValueError, AttributeError):
                pass
        
        return cls(
            doi=data.get("doi", ""),
            inspire_url=data.get("inspire_url"),
            authors=data.get("authors", []),
            publish_year=publish_year,
            publish_month=publish_month
        )
    
    def get_publish_year(self) -> Optional[int]:
        """
        获取发布年份
        
        Returns:
            发布年份，如果没有则返回 None
        """
        return self.publish_year
    
    def get_publish_date_str(self) -> str:
        """
        获取发布日期字符串
        
        Returns:
            格式化的日期字符串
        """
        if self.publish_year is None:
            return "未知"
        if self.publish_month is not None:
            return f"{self.publish_year}-{self.publish_month:02d}"
        return str(self.publish_year)
    
    def get_recency_score(self, reference_year: Optional[int] = None) -> float:
        """
        计算论文的时效性得分 (0.0 - 1.0)
        
        更新的论文得分更高。使用指数衰减函数。
        
        Args:
            reference_year: 参考年份，默认为当前年份
            
        Returns:
            时效性得分，范围 [0.0, 1.0]
        """
        publish_year = self.get_publish_year()
        if publish_year is None:
            return 0.5  # 如果没有日期信息，返回中性得分
        
        if reference_year is None:
            reference_year = datetime.now().year
        
        # 计算论文年龄
        age = reference_year - publish_year
        
        # 使用指数衰减：半衰期为5年
        # score = 0.5^(age/5)
        # 这样：当前年份=1.0, 5年前≈0.5, 10年前≈0.25
        if age < 0:
            return 1.0  # 未来的日期（数据错误）
        
        half_life = 5.0
        score = 0.5 ** (age / half_life)
        
        return min(max(score, 0.0), 1.0)  # 限制在 [0, 1] 范围内


def sanitize_filename(title: str) -> str:
    """
    Sanitize filename to match the downloader's behavior.
    Replaces illegal characters with '_' and truncates to 150 chars.
    """
    sane_title = re.sub(r'[\\/:*?"<>|#&]', '_', title)
    sane_title = (sane_title[:150] + '..') if len(sane_title) > 150 else sane_title
    return sane_title


class MetadataManager:
    """元数据管理器"""
    
    def __init__(self):
        """初始化元数据管理器"""
        self.metadata_cache: Dict[str, PaperMetadata] = {}
    
    def load_metadata_file(self, metadata_file: Path) -> bool:
        """
        从JSON文件加载元数据
        
        支持两种格式：
        1. 新格式（items数组）：{"items": [{title, doi, authors, published: {year, month}}]}
        2. 旧格式（文件名映射）：{"filename.md": {doi, authors, publish_date}}
        
        Args:
            metadata_file: 元数据JSON文件路径
            
        Returns:
            加载是否成功
        """
        if not metadata_file.exists():
            print(f"    ℹ️  元数据文件不存在: {metadata_file}")
            return False
        
        try:
            with open(metadata_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 检测是否为新格式（包含items数组）
            if isinstance(data, dict) and "items" in data:
                # 新格式：{"items": [{"title": "...", "doi": "...", ...}]}
                items = data.get("items", [])
                for item in items:
                    if not isinstance(item, dict):
                        continue
                    
                    # 使用title作为文件名（需要添加.md扩展名）
                    title = item.get("title", "")
                    if not title:
                        continue
                    
                    # 将title转换为有效的文件名
                    clean_title = sanitize_filename(title)
                    filename = f"{clean_title}.md"
                    
                    metadata = PaperMetadata.from_dict(item)
                    self.metadata_cache[filename] = metadata
            
            elif isinstance(data, dict):
                # 旧格式：{"filename.md": {"doi": "...", ...}}
                for filename, metadata_dict in data.items():
                    metadata = PaperMetadata.from_dict(metadata_dict)
                    self.metadata_cache[filename] = metadata
            
            print(f"    ✓ 已加载 {len(self.metadata_cache)} 条元数据记录")
            return True
            
        except Exception as e:
            print(f"    ⚠️  加载元数据文件失败: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def get_metadata(self, paper_filename: str) -> Optional[PaperMetadata]:
        """
        获取指定论文的元数据
        
        Args:
            paper_filename: 论文文件名（含扩展名）
            
        Returns:
            元数据对象，如果不存在则返回 None
        """
        # 尝试完整文件名
        if paper_filename in self.metadata_cache:
            return self.metadata_cache[paper_filename]
        
        # 尝试只用文件名（不含路径）
        filename_only = Path(paper_filename).name
        if filename_only in self.metadata_cache:
            return self.metadata_cache[filename_only]
        
        return None
    
    def add_metadata(self, paper_filename: str, metadata: PaperMetadata):
        """
        添加或更新论文元数据
        
        Args:
            paper_filename: 论文文件名
            metadata: 元数据对象
        """
        self.metadata_cache[paper_filename] = metadata
    
    def sort_papers_by_recency(
        self,
        papers: List[Dict[str, Any]],
        descending: bool = True
    ) -> List[Dict[str, Any]]:
        """
        按发布时间对论文列表进行排序
        
        Args:
            papers: 论文列表
            descending: True表示从新到旧，False表示从旧到新
            
        Returns:
            排序后的论文列表
        """
        def get_sort_key(paper: Dict[str, Any]) -> tuple:
            """
            生成排序键
            
            Returns:
                (年份, 原始索引) - 没有元数据的论文会被放在最后
            """
            filename = Path(paper.get('md_filename', '')).name
            metadata = self.get_metadata(filename)
            
            if metadata:
                year = metadata.get_publish_year()
                if year is not None:
                    return (year, 0)
            
            # 没有元数据的论文使用一个很小/很大的年份
            return (-9999 if descending else 9999, 1)
        
        sorted_papers = sorted(
            papers,
            key=get_sort_key,
            reverse=descending
        )
        
        return sorted_papers
    
    def get_papers_with_metadata(
        self,
        papers: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        为论文列表添加元数据信息
        
        Args:
            papers: 原始论文列表
            
        Returns:
            添加了元数据字段的论文列表
        """
        enriched_papers = []
        
        for paper in papers:
            # 创建副本以避免修改原始数据
            enriched_paper = paper.copy()
            
            filename = Path(paper.get('md_filename', '')).name
            metadata = self.get_metadata(filename)
            
            if metadata:
                enriched_paper['metadata'] = metadata.to_dict()
                enriched_paper['recency_score'] = metadata.get_recency_score()
            else:
                enriched_paper['metadata'] = None
                enriched_paper['recency_score'] = 0.5  # 默认中性得分
            
            enriched_papers.append(enriched_paper)
        
        return enriched_papers
    
    def export_metadata(self, output_file: Path):
        """
        导出元数据到JSON文件
        
        Args:
            output_file: 输出文件路径
        """
        data = {
            filename: metadata.to_dict()
            for filename, metadata in self.metadata_cache.items()
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"    ✓ 元数据已导出到: {output_file}")
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        获取元数据统计信息
        
        Returns:
            统计信息字典
        """
        total = len(self.metadata_cache)
        with_dates = sum(1 for m in self.metadata_cache.values() if m.publish_year is not None)
        
        years = [m.get_publish_year() for m in self.metadata_cache.values()]
        valid_years = [y for y in years if y is not None]
        
        stats = {
            "total_papers": total,
            "papers_with_dates": with_dates,
            "year_range": (min(valid_years), max(valid_years)) if valid_years else None,
            "avg_recency_score": sum(m.get_recency_score() for m in self.metadata_cache.values()) / total if total > 0 else 0
        }
        
        return stats
    
    def print_statistics(self):
        """打印元数据统计信息"""
        stats = self.get_statistics()
        
        print("\n📊 元数据统计:")
        print(f"  - 总论文数: {stats['total_papers']}")
        print(f"  - 有日期信息: {stats['papers_with_dates']}/{stats['total_papers']}")
        
        if stats['year_range']:
            print(f"  - 年份范围: {stats['year_range'][0]} - {stats['year_range'][1]}")
        
        print(f"  - 平均时效性得分: {stats['avg_recency_score']:.3f}")
