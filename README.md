# Check-Mentor

**Check-Mentor** 是一个统一的学术开盒流水线，旨在帮助用户快速分析教授的研究贡献、领域热点以及适合本科生的科研项目。

核心流程：从 DOI 下载论文 → PDF 转 Markdown → 合并元数据 → LLM 工作流分析 → 生成中/英文报告。

本项目已将所有功能整合到 `main.py` 统一入口。

## 🚀 快速开始

### 1. 安装依赖

```powershell
python -m pip install -r requirements.txt
```

主要依赖：
- **LangChain + OpenAI**: 用于核心分析与报告生成。
- **MinerU (Magic-PDF)**: 用于高质量 PDF 转 Markdown。
- **InspireHEP / CrossRef / OpenAlex**: 用于元数据获取与文献检索。

### 2. 配置环境

1.  **LLM 配置**:
    在根目录复制 `.env.example` 为 `.env`，并填入以下信息：
    ```ini
    OPENAI_API_KEY="sk-..."
    OPENAI_API_BASE="https://api.openai.com/v1"
    LLM_MODEL="gpt-4o"
    # 可选：备用模型（如阿里云百炼）
    DASHSCOPE_API_KEY="..."
    LLM_FALLBACK_MODEL="qwen-plus"
    ```

2.  **MinerU 配置**:
    设置环境变量 `MINERU_TOKEN`，或者在运行命令时通过 `--token` 参数传入。

3.  **下载配置 (可选)**:
    修改 `config.ini` 以调整下载行为（如 Top-N 筛选、并发数等）。

### 3. 数据准备

在 `data/` 目录下创建以教授姓名命名的文件夹（如 `data/张三`），并建立以下子目录：
- `main/`: 教授的核心代表作。
- `ref1/`: 领域热点相关的参考文献。
- `cited/`: 适合本科生项目的被引文献。

或者使用自动化工具（见下文）自动下载并整理。

---

## 🛠️ 命令详解

所有操作均通过 `python main.py <command>` 执行。

### 1. 下载论文 (通用领域)

从 DOI 下载 PDF 并自动整理目录。

```powershell
# 从 results.txt 自动读取并下载
python main.py download --from-results AUTO --workers 6 --depth 1 --pdf-root .\Downloads_pdf

# 手动指定 DOI 下载
python main.py download --doi "10.1038/nphys4074" --teacher "示例老师" --depth 1
```

### 2. 下载论文 (高能物理/InspireHEP) ⚛️

针对高能物理领域，支持从 InspireHEP 批量下载并自动生成元数据。

```powershell
# 从 mid.txt 批量下载
python main.py meta-pack --mid-file .\inspirehep_source\pre-process\mid.txt --k 5 --token "YOUR_MINERU_TOKEN"

# 指定老师和 DOI
python main.py meta-pack --teacher "曹庆宏" --dois "10.1103/PhysRevLett.116.061102" --k 3
```

### 3. PDF 转 Markdown

使用 MinerU 将下载的 PDF 转换为 Markdown 格式，以便 LLM 分析。

```powershell
# 如果已在 .env 配置 MINERU_TOKEN，可省略 --token
python main.py pdf2md --teacher "示例老师" --pdf-root .\Downloads_pdf --md-root .\data --subdirs main,ref1,cited
```
```

### 4. 合并历史记录

将下载记录与转换后的 Markdown 数据关联，生成完整的元数据。

```powershell
python main.py merge-history --teacher "示例老师" --subdir main
python main.py merge-history --teacher "示例老师" --subdir ref1
python main.py merge-history --teacher "示例老师" --subdir cited
```

### 5. 清理中间文件

清理 `data/` 目录下的中间文件（如 .zip, .pdf, images 等），仅保留 `.md` 和 `history.json`，以节省空间并保持目录整洁。

```powershell
python main.py clean --target "示例老师"
```

### 6. 运行分析

启动 LLM 工作流，生成最终报告。

```powershell
# 完整分析
python main.py analyze --target "示例老师"

# 测试模式（仅分析少量论文，快速验证）
python main.py analyze --target "示例老师" --test-mode
```

### 7. 一条龙运行 (Run All)

自动执行：PDF转MD -> 合并历史 -> 清理中间文件 -> 分析。

```powershell
python main.py run-all --target "示例老师" --token "YOUR_MINERU_TOKEN" --test-mode
```

---

## 📂 目录结构

```
Check-Mentor/
├── main.py                 # 统一入口脚本
├── config.ini              # 配置文件
├── requirements.txt        # 依赖列表
├── core/                   # 核心分析逻辑 (LLM Workflows)
│   ├── workflow_orchestrator.py
│   └── workflows/
├── data/                   # Markdown 数据与元数据 (分析输入)
│   └── 示例老师/
│       ├── main/
│       ├── ref1/
│       └── cited/
├── Downloads_pdf/          # PDF 下载目录
├── DOI_source/             # 通用下载器源码
├── inspirehep_source/      # InspireHEP 下载器源码
├── tools/                  # 辅助工具 (pdf2md 等)
└── output/                 # 最终报告输出
```

## ✨ 特性

- **多源支持**: 支持通用 DOI 下载与 InspireHEP 深度集成。
- **智能分析**: 三大工作流分别分析教授贡献、领域热点与本科生项目。
- **自动化**: 从 PDF 到最终报告的全流程自动化。
- **元数据增强**: 利用元数据（发表时间、作者等）提升分析准确性。
- **聚类分析**: 自动对大量论文进行聚类与采样，处理大规模文献集。

## ❓ 常见问题

1.  **缺少依赖**: 请确保执行了 `pip install -r requirements.txt`。
2.  **MinerU Token**: 必须提供 Token 才能进行 PDF 转 Markdown。可申请 MinerU API 权限。
3.  **分析报错**: 检查 `.env` 文件中的 OpenAI Key 是否正确配置。
4.  **路径问题**: 默认数据路径为 `data/`，下载路径为 `Downloads_pdf/`。可通过参数自定义。

---
*Powered by Check-Mentor Team*
