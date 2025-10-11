"""
配置文件：存储项目的所有配置参数
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 项目根目录
BASE_DIR = Path(__file__).parent

# API 配置
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4-turbo-preview")

# 可选的 Tavily API
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")

# 搜索配置
MAX_PAPERS_PER_SOURCE = 10  # 每个来源最多获取的论文数
RECENT_YEARS = 5  # 分析最近几年的论文

# 报告输出配置
REPORTS_DIR = BASE_DIR / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

# 缓存配置
CACHE_DIR = BASE_DIR / "cache"
CACHE_DIR.mkdir(exist_ok=True)

# Agent 配置
MAX_ITERATIONS = 5  # Agent 最大迭代次数
TEMPERATURE = 0.3  # LLM 温度参数（越低越严谨）

# 爬虫配置
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
REQUEST_TIMEOUT = 30  # 请求超时时间（秒）
