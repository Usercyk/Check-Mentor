# 学术开盒项目 - 论文分析模块

本模块负责任务 1-5：使用 RAG 技术对导师论文进行智能分析。

## 功能说明

### 任务 1：论文加载
- 从指定目录加载论文文件
- **支持格式**：PDF 和 Markdown (.md)
- 自动提取文本内容并保留元数据（作者、标题、年份等）

### 任务 2：文本分块
- 使用递归字符分割器将长文本切分成合适的块
- 块大小：1000 字符
- 重叠：200 字符

### 任务 3：向量化嵌入
- 使用 OpenAI Embeddings (text-embedding-3-small) 将文本转换为向量
- 支持语义搜索和相似度计算

### 任务 4：向量存储
- 使用 Chroma 向量数据库持久化存储
- 支持高效的相似度检索

### 任务 5：相关性分析
- 基于 5 个核心维度评估论文与教授研究的相关性：
  1. **研究领域匹配** (权重 0.3)
  2. **技术方法匹配** (权重 0.25)
  3. **创新性** (权重 0.2)
  4. **新手友好度** (权重 0.15)
  5. **实用价值** (权重 0.1)

## 安装依赖

```powershell
# 安装所有依赖
pip install -r requirements.txt
```

## 配置

1. 复制 `.env.example` 为 `.env`：
```powershell
cp .env.example .env
```

2. 编辑 `.env` 文件，填入你的 API 密钥：
```
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

## 使用方法

### 1. 准备论文文件
将要分析的论文文件放入对应目录：

**选项 A: 使用 Markdown 文件（推荐）**
```powershell
# 创建目录
mkdir -p data/papers

# 将 Markdown 文件复制到该目录
cp /path/to/papers/*.md data/papers/
```

**选项 B: 使用 PDF 文件**
```powershell
# 创建目录
mkdir -p data/pdfs

# 将 PDF 文件复制到该目录
cp /path/to/papers/*.pdf data/pdfs/
```

### 2. 配置文件类型
编辑 `main.py`，设置要使用的文件类型：
```python
# 在 main.py 中找到这一行：
file_type = "md"  # 使用 Markdown 文件
# 或
file_type = "pdf"  # 使用 PDF 文件
```
### 3. 运行分析程序
```powershell
python main.py
```

### 4. 查看结果
- **数据文件**：`professor_research_data.json` - 包含所有分析结果
- **向量存储**：`./chroma_db/` - Chroma 向量数据库
- **分析摘要**：`output/analysis_summary.md` - 可读的分析报告

## 目录结构

```
Check-Mentor/
├── config.py              # 配置管理
├── core_questions.py      # 核心评估维度定义
├── rag_processor.py       # RAG 处理器（主要逻辑）
├── data_manager.py        # 数据持久化管理
├── main.py               # 主程序入口
├── requirements.txt      # 依赖列表
├── .env.example         # 环境变量模板
├── .env                 # 环境变量（不提交到 git）
├── data/                # 数据目录
│   ├── papers/         # Markdown 文件存放处
│   └── pdfs/           # PDF 文件存放处
├── output/             # 输出文件
├── chroma_db/          # 向量数据库
└── professor_research_data.json  # 分析结果
```

## 代码架构

### core_questions.py
定义 5 个评估维度及其对应的问题：
```python
from core_questions import get_question, get_all_questions, get_question_weight

# 获取单个问题
question = get_question("research_domain", lang="zh")

# 获取所有问题
all_questions = get_all_questions(lang="zh")

# 获取权重
weight = get_question_weight("research_domain")  # 0.3
```

### config.py
集中管理配置：
```python
import config

# API 配置
api_key = config.OPENAI_API_KEY
embedding_model = config.EMBEDDING_MODEL  # text-embedding-3-small
llm_model = config.LLM_MODEL  # gpt-4

# 路径配置
data_dir = config.DATA_DIR
output_dir = config.OUTPUT_DIR

# 验证配置
config.validate_config()
```

### rag_processor.py
核心 RAG 处理逻辑：
```python
from rag_processor import PaperRAGProcessor

processor = PaperRAGProcessor()

# 加载 PDF
docs = processor.load_papers_from_directory("data/pdfs")

# 分块
splits = processor.split_documents(docs)

# 创建向量存储
vectorstore = processor.create_vectorstore(splits)

# 分析相关性
analysis = processor.analyze_paper_relevance(paper_id, paper_title, professor_interests)
```

### data_manager.py
数据持久化：
```python
from data_manager import DataManager

manager = DataManager("results.json")

# 设置教授信息
manager.set_professor_info(name="张教授", department="物理系")

# 添加论文
manager.add_paper({"id": "p1", "title": "论文标题"})

# 添加分析结果
manager.add_analysis_result("p1", analysis_data)

# 保存
manager.save()
```

## 输出格式

分析结果 JSON 结构：
```json
{
  "metadata": {
    "project": "学术开盒",
    "version": "1.0",
    "created_at": "2025-01-01T12:00:00"
  },
  "professor_info": {
    "name": "张教授",
    "department": "物理系",
    "research_areas": ["量子计算", "凝聚态物理"]
  },
  "papers": [
    {
      "id": "paper_001",
      "title": "Quantum Computing Advances",
      "summary": "论文摘要..."
    }
  ],
  "analysis_results": {
    "paper_001": {
      "relevance_analysis": {
        "score": 8.5,
        "confidence": 0.9,
        "evidence": ["证据1", "证据2"],
        "reasoning": "分析理由..."
      }
    }
  }
}
```

## 注意事项

1. **API 密钥安全**：永远不要将 `.env` 文件提交到 git
2. **成本控制**：OpenAI API 按使用量计费，大量论文分析会产生费用
3. **内存使用**：处理大量 PDF 时注意内存占用
4. **向量存储**：`chroma_db/` 目录会随着论文数量增长

## 扩展开发

如果需要添加新的评估维度，在 `core_questions.py` 中修改 `CORE_QUESTIONS` 字典：

```python
CORE_QUESTIONS = {
    "your_new_dimension": {
        "weight": 0.15,
        "question_en": "Your question in English",
        "question_zh": "你的中文问题"
    }
}
```

## 许可证

本项目为学术研究使用。
