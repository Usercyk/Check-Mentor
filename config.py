"""""""""

配置管理模块

从 .env 文件加载环境变量配置管理模块配置模块

"""

import os加载环境变量和系统配置从 .env 文件加载环境变量

from pathlib import Path

from dotenv import load_dotenv""""""



# 加载 .env 文件import osimport os

load_dotenv()

from pathlib import Pathfrom dotenv import load_dotenv

# 项目信息

PROJECT_NAME = "学术开盒 - Check-Mentor"from dotenv import load_dotenv

PROJECT_VERSION = "1.0"

# 加载 .env 文件

# API 配置

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")# 加载 .env 文件load_dotenv()

OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")

load_dotenv()

# LLM 配置

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")# --- LLM Provider ---

LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4")

LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.3"))# API 配置# 使用 'openai' 或 'gemini'



# Embedding 配置OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

EMBEDDING_API_KEY = os.getenv("EMBEDDING_API_KEY", OPENAI_API_KEY)OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")

EMBEDDING_API_BASE = os.getenv("EMBEDDING_API_BASE", OPENAI_API_BASE)

LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4")# --- OpenAI/School Platform API ---

# Gemini 配置（备用）

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")



# 向量数据库配置OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")

CHROMA_PERSIST_DIRECTORY = os.getenv("CHROMA_PERSIST_DIRECTORY", "./chroma_db")

CHROMA_COLLECTION_NAME = os.getenv("CHROMA_COLLECTION_NAME", "papers")# Embedding 配置LLM_MODEL = os.getenv("LLM_MODEL", "gpt-3.5-turbo")



# 文本分割配置EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))

CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))EMBEDDING_API_KEY = os.getenv("EMBEDDING_API_KEY", OPENAI_API_KEY)# --- Google Gemini API ---



# 路径配置EMBEDDING_API_BASE = os.getenv("EMBEDDING_API_BASE", OPENAI_API_BASE)GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"

OUTPUT_DIR = BASE_DIR / "output"

CACHE_DIR = BASE_DIR / "cache"# Gemini 配置# --- Tavily Search API ---



# 创建必要的目录GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

CACHE_DIR.mkdir(exist_ok=True, parents=True)



# 向量数据库配置# --- gpt-researcher Configuration ---

def validate_config():

    """验证配置是否完整"""CHROMA_PERSIST_DIRECTORY = os.getenv("CHROMA_PERSIST_DIRECTORY", "./chroma_db")# 可选值: "tavily", "duckduckgo", "google", "bing", "arxiv", "serper", "semantic_scholar", "pubmed", "exa"

    required_vars = {

        "OPENAI_API_KEY": OPENAI_API_KEY,CHROMA_COLLECTION_NAME = os.getenv("CHROMA_COLLECTION_NAME", "papers")SEARCH_PROVIDER = os.getenv("SEARCH_PROVIDER", "duckduckgo")

    }

    

    missing_vars = [var for var, value in required_vars.items() if not value]

    # 项目配置# 报告类型: "research_report", "resource_report", "outline_report", "custom_report", "subtopic_report"

    if missing_vars:

        raise ValueError(PROJECT_NAME = os.getenv("PROJECT_NAME", "学术开盒")REPORT_TYPE = "research_report"

            f"Missing required environment variables: {', '.join(missing_vars)}\n"

            f"Please check your .env file."PROJECT_VERSION = "1.0"

        )

    MAX_PAPERS = int(os.getenv("MAX_PAPERS", "100"))# --- 检查关键配置 ---

    print("✓ Configuration validated successfully")

def check_config():

# 路径配置    """检查必要的 API 密钥是否已配置"""

BASE_DIR = Path(__file__).parent    if LLM_PROVIDER == "openai" and not OPENAI_API_KEY:

DATA_DIR = BASE_DIR / "data"        raise ValueError("LLM_PROVIDER 设置为 'openai'，但 OPENAI_API_KEY 未在 .env 文件中配置。")

OUTPUT_DIR = BASE_DIR / "output"    if LLM_PROVIDER == "gemini" and not GEMINI_API_KEY:

CACHE_DIR = BASE_DIR / "cache"        raise ValueError("LLM_PROVIDER 设置为 'gemini'，但 GEMINI_API_KEY 未在 .env 文件中配置。")

    

# 确保目录存在    # Tavily 是一个推荐的搜索引擎，如果使用它，需要检查 key

DATA_DIR.mkdir(exist_ok=True)    if SEARCH_PROVIDER == "tavily" and not TAVILY_API_KEY:

OUTPUT_DIR.mkdir(exist_ok=True)        print("⚠️ 警告: 搜索提供商设置为 'tavily'，但 TAVILY_API_KEY 未配置。将回退到 'duckduckgo'。")

CACHE_DIR.mkdir(exist_ok=True)        return "duckduckgo"

        

# 文本分割配置    return SEARCH_PROVIDER

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200# 在模块加载时执行检查

try:

# 检索配置    SEARCH_PROVIDER = check_config()

TOP_K_CHUNKS = 5  # 每次检索返回的文本块数量except ValueError as e:

    print(f"❌ 配置错误: {e}")

# 论文总结配置    # 在 Streamlit 应用中，我们可能希望显示错误而不是直接退出

SUMMARY_MAX_TOKENS = 500    # 这里只打印错误，让应用本身来处理

    pass



def validate_config():
    """验证配置是否完整"""
    errors = []
    
    if not OPENAI_API_KEY and LLM_PROVIDER == "openai":
        errors.append("OPENAI_API_KEY is required when using OpenAI provider")
    
    if not GEMINI_API_KEY and LLM_PROVIDER == "gemini":
        errors.append("GEMINI_API_KEY is required when using Gemini provider")
    
    if not EMBEDDING_API_KEY:
        errors.append("EMBEDDING_API_KEY is required")
    
    if errors:
        raise ValueError("Configuration errors:\n" + "\n".join(f"  - {e}" for e in errors))
    
    return True


if __name__ == "__main__":
    print("Configuration:")
    print(f"  LLM Provider: {LLM_PROVIDER}")
    print(f"  LLM Model: {LLM_MODEL}")
    print(f"  Embedding Model: {EMBEDDING_MODEL}")
    print(f"  Chroma Directory: {CHROMA_PERSIST_DIRECTORY}")
    print(f"  Base Directory: {BASE_DIR}")
    
    try:
        validate_config()
        print("\n✓ Configuration is valid")
    except ValueError as e:
        print(f"\n✗ {e}")
