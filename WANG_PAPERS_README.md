# 王剑威老师论文分析说明

## 📚 论文数据

从 main 分支复制的王剑威老师的论文数据：

```
Downloads_md/王剑威/
├── main/                  # 主要论文（3篇）
│   ├── Error-protected qubits in a silicon photonic chip.md
│   ├── Scaling quantum computers with electronic–photonic chips.md
│   └── Topologically protected quantum entanglement emitters.md
├── ref1/                  # 一级引用论文（65篇）
│   ├── 16-qubit IBM universal quantum computer can be fully entangled.md
│   ├── 3D integration enables ultralow-noise isolator-free lasers in silicon photonics.md
│   └── ... (63 more papers)
└── ref2/                  # 二级引用论文（5篇）
    ├── A trusted node–free eight-user metropolitan quantum communication network.md
    ├── Quantum Verification and Estimation with Few Copies.md
    └── ... (3 more papers)
```

**总计：73 篇论文**

## 🚀 使用方法

### 1. 确保环境配置

确保 `.env` 文件已配置好 OpenAI API 密钥：

```bash
OPENAI_API_KEY=your_api_key_here
```

### 2. 运行分析程序

```powershell
python process_wang_papers.py
```

### 3. 程序流程

程序会执行以下步骤：

1. **扫描论文**：自动扫描 `Downloads_md/王剑威/` 下的所有论文
2. **显示统计**：显示每个类别的论文数量
3. **询问确认**：询问是否继续完整分析（需要消耗 API）
4. **RAG 处理**：
   - 加载所有 73 篇论文
   - 将论文分割成文本块
   - 创建向量嵌入
   - 存储到 Chroma 向量数据库
5. **生成结果**：
   - 为每篇论文生成摘要（任务一）
   - 分析每篇论文的相关性（任务二，5个维度）
   - 保存到 JSON 文件

## 📊 输出文件

分析完成后会生成：

1. **wang_jianwei_research_data.json**
   - 完整的分析结果
   - 符合 TODO.md 规定的 JSON 结构
   - 包含所有 73 篇论文的元数据、摘要和分析

2. **wang_jianwei_analysis_summary.md**
   - 可读的分析报告摘要
   - Markdown 格式

3. **chroma_db/**
   - Chroma 向量数据库
   - 包含所有论文的向量嵌入
   - 可用于后续检索

## 🔍 数据结构

生成的 JSON 文件结构：

```json
{
  "metadata": {
    "project_version": "1.0",
    "created_date": "2025-10-21T...",
    "last_updated": "2025-10-21T...",
    "total_papers": 73,
    "analysis_model": "gpt-4",
    "embedding_model": "text-embedding-3-small",
    "data_sources": ["Downloads_md/王剑威"]
  },
  
  "professor_info": {
    "name": "王剑威",
    "department": "物理学院",
    "university": "北京大学",
    "research_areas": ["量子计算", "光子学", "量子纠缠", "硅光子芯片"],
    "position": "副教授"
  },
  
  "papers": [
    {
      "id": "paper_001",
      "title": "Error-protected qubits in a silicon photonic chip",
      "category": "main",
      "md_filename": "Error-protected qubits in a silicon photonic chip.md",
      "authors": [...],
      "year": 2021,
      "summary": {
        "summary": "论文摘要...",
        "timestamp": "..."
      }
    }
    // ... 72 more papers
  ],
  
  "analysis_results": {
    "paper_001": {
      "research_domain": {
        "score": 0.92,
        "confidence": 0.88,
        "evidence": "...",
        "reasoning": "..."
      },
      "technical_approach": {...},
      "novelty": {...},
      "beginner_friendly": {...},
      "practical_value": {...}
    }
    // ... 72 more papers
  },
  
  "correlation_data": {},
  "report_cache": {}
}
```

## ⚠️ 注意事项

1. **API 消耗**：
   - 处理 73 篇论文会消耗大量 API credits
   - 建议先用少量论文测试

2. **处理时间**：
   - 完整处理 73 篇论文可能需要 1-2 小时
   - 取决于网络速度和 API 响应时间

3. **中断恢复**：
   - 如果处理中断，向量库已保存的部分不会丢失
   - 但需要重新运行整个流程

4. **论文位置**：
   - Downloads_md/ 目录在 .gitignore 中
   - 论文文件不会提交到 git
   - 需要从 main 分支复制或重新下载

## 🧪 测试模式

如果想先测试几篇论文：

1. 修改 `process_wang_papers.py` 中的扫描逻辑
2. 只处理 main 目录（3篇论文）
3. 或者限制每个类别的论文数量

示例修改：

```python
# 在 scan_papers_directory 函数中
for md_file in md_files[:3]:  # 只取前3篇
    # ...
```

## 📈 后续步骤

分析完成后，可以：

1. 查看 JSON 文件中的分析结果
2. 使用向量数据库进行语义检索
3. 实现任务三：生成最终报告
4. 可视化分析结果
