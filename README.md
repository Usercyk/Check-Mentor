# 🎓 学术开盒 (Check-Mentor)

> **为物理学本科生准备的导师研究分析工具**

一个基于 AI 的自动化工具，帮助物理学本科生快速了解导师的研究方向、代表性贡献，以及适合的科研入门路径。

## ✨ 核心功能

本项目通过分析导师的学术论文，自动生成一份面向本科生的研究报告，回答四个核心问题：

1. **这位老师近期的研究兴趣是什么？**
   - 自动分析最近 3-5 年的论文，总结主要研究方向

2. **在这些方向上，老师有哪些代表性贡献？**
   - 识别高被引论文，总结关键学术成果

3. **这些方向的核心问题是什么？——学术界在关心什么？**
   - 深度分析领域前沿问题和技术挑战

4. **有哪些适合本科生切入的科研任务？**
   - AI 设计循序渐进的入门任务（文献调研、代码复现、数据分析等）

## 🏗️ 技术架构

```
学术开盒
├── 数据层: 学术爬虫
│   ├── Google Scholar (论文 + 引用)
│   └── arXiv (预印本)
│
├── 核心层: LangGraph Multi-Agent System
│   ├── 数据收集代理 (Data Collector)
│   ├── 研究分析代理 (Research Analyzer)
│   ├── 本科生导师代理 (Mentor)
│   └── 报告生成器 (Report Generator)
│
└── 表现层: Streamlit Web App
    └── 友好的用户界面
```

**核心技术栈**:
- **LangChain/LangGraph**: 多代理协作框架
- **OpenAI GPT-4**: 深度分析和报告生成
- **Scholarly**: Google Scholar 数据获取
- **arXiv API**: 预印本论文检索
- **Streamlit**: Web 用户界面

## 🚀 快速开始

### 1. 环境准备

```powershell
# 克隆项目（如果是从 Git）
# git clone <repo-url>
cd Check-Mentor

# 创建虚拟环境（推荐）
python -m venv venv
.\venv\Scripts\Activate.ps1

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置 API Key

复制 `.env.example` 为 `.env`，并填入你的 OpenAI API Key:

```powershell
copy .env.example .env
```

编辑 `.env` 文件:
```env
OPENAI_API_KEY=sk-your-api-key-here
LLM_MODEL=gpt-4-turbo-preview
```

**获取 API Key**:
- 访问 [OpenAI Platform](https://platform.openai.com/api-keys)
- 或使用兼容 OpenAI 的其他服务（如 Azure OpenAI, 国内代理等）

### 3. 运行应用

**方式一：Web 界面（推荐）**
```powershell
streamlit run app.py
```
然后在浏览器中打开 `http://localhost:8501`

**方式二：命令行**
```powershell
python workflow.py "Zhang Wei"
```

## 📖 使用示例

### Web 界面使用

1. 启动应用: `streamlit run app.py`
2. 在输入框中输入导师的**英文姓名**（如: `Zhang Wei`）
3. 点击"开始分析"
4. 等待 2-5 分钟，AI 将：
   - 🔍 搜索论文（Google Scholar + arXiv）
   - 📊 分析研究方向
   - 🏆 总结关键贡献
   - 🎯 分析领域问题
   - 🚀 设计科研任务
5. 下载生成的 Markdown 报告

### 命令行使用

```powershell
# 基本用法
python workflow.py "Professor Name"

# 示例
python workflow.py "Qi-Kun Xue"
```

报告将自动保存到 `reports/` 目录。

## 📊 生成报告示例

报告包含以下部分：

```markdown
# 🎓 张三 教授学术档案

## 📋 基本信息
- 姓名: Zhang San
- 所属机构: Peking University
- 研究兴趣: Topological Materials, Quantum Transport
...

## 🔬 一、近期研究方向
1. 拓扑量子材料: 研究新型拓扑绝缘体...
2. 量子输运现象: 探索低维系统...
...

## 🏆 二、代表性学术贡献
...

## 🎯 三、领域核心问题与挑战
...

## 🚀 四、本科生科研入门建议
### 任务 1: 拓扑绝缘体文献综述
- 描述: 阅读并总结拓扑绝缘体的基本概念...
- 预期成果: 3000字文献综述
- 预计时间: 2-3周
...

## 📚 五、重要论文列表
...
```

## ⚙️ 配置选项

在 `config.py` 中可以调整：

```python
MAX_PAPERS_PER_SOURCE = 10  # 每个来源最多获取的论文数
RECENT_YEARS = 5            # 分析最近几年的论文
LLM_MODEL = "gpt-4-turbo-preview"  # 使用的 LLM 模型
TEMPERATURE = 0.3           # LLM 温度（越低越严谨）
```

## 🔧 项目结构

```
Check-Mentor/
├── scrapers/              # 学术数据爬虫
│   ├── __init__.py       # 数据结构定义
│   ├── scholar_scraper.py # Google Scholar 爬虫
│   └── arxiv_scraper.py   # arXiv 爬虫
│
├── agents/                # LangGraph Agents
│   ├── __init__.py       # Agent 状态定义
│   ├── data_collector.py # 数据收集代理
│   ├── research_analyzer.py # 研究分析代理
│   └── mentor_agent.py   # 本科生导师代理
│
├── workflow.py           # 主工作流
├── report_generator.py   # 报告生成器
├── app.py               # Streamlit Web 应用
├── config.py            # 配置文件
├── requirements.txt     # 依赖列表
├── .env.example         # 环境变量模板
└── reports/             # 生成的报告（自动创建）
```

## 💰 成本估算

使用 OpenAI API 的成本：

- **GPT-4 Turbo**: 约 $0.01/1K tokens (input), $0.03/1K tokens (output)
- **单次分析**: 预计 10K-30K tokens
- **成本**: 约 **$0.2 - $1.0 美元/报告**

比订阅 Gemini Ultra ($250/月) 便宜得多！

## 🛠️ 故障排除

### 1. 找不到导师

**问题**: `❌ 未找到 XXX 的 Scholar 主页`

**解决**:
- 检查姓名拼写是否正确
- 尝试使用导师常用的英文名变体
- 确认导师有 Google Scholar 主页

### 2. API 调用失败

**问题**: `OpenAI API 调用失败`

**解决**:
- 检查 `.env` 中的 `OPENAI_API_KEY` 是否正确
- 确认 API Key 有足够的余额
- 检查网络连接（可能需要代理）

### 3. 爬虫被封禁

**问题**: Google Scholar 返回 403 错误

**解决**:
- 在 `scholar_scraper.py` 中启用代理
- 减少 `MAX_PAPERS_PER_SOURCE`
- 增加请求间隔时间

## 🚧 未来计划

- [ ] 支持更多数据源（Web of Science, Scopus）
- [ ] 添加校园网代理支持
- [ ] 支持中文导师姓名搜索
- [ ] 生成 PDF 格式报告
- [ ] 添加导师对比功能
- [ ] 构建导师数据库缓存

## 📝 许可证

MIT License

## 🙏 致谢

本项目受到"让选择不再迷茫"的愿景驱动，致力于帮助物理学本科生找到真正适合自己的科研方向。

---

**💡 提示**: 本报告由 AI 自动生成，建议结合导师个人主页和代表性论文进行深入了解，并与导师进行面对面交流。

**祝你的科研之旅一帆风顺！🌟**
