# 项目结构说明

## 📂 完整目录结构

```
Check-Mentor/
│
├── 📄 核心文件
│   ├── main.py                 # 命令行入口
│   ├── workflow.py             # 主工作流（LangGraph）
│   ├── config.py               # 配置文件
│   └── report_generator.py    # 报告生成器
│
├── 🕷️ 爬虫模块 (scrapers/)
│   ├── __init__.py            # 数据结构定义 (Paper, ProfessorProfile)
│   ├── scholar_scraper.py     # Google Scholar 爬虫
│   └── arxiv_scraper.py       # arXiv 预印本爬虫
│
├── 🤖 AI 代理 (agents/)
│   ├── __init__.py            # Agent 状态定义 (AgentState)
│   ├── data_collector.py      # 数据收集代理
│   ├── research_analyzer.py   # 研究分析代理（LLM）
│   └── mentor_agent.py        # 本科生导师代理（LLM）
│
├── 🌐 用户界面
│   └── app.py                 # Streamlit Web 应用
│
├── 📝 配置与文档
│   ├── .env                   # 环境变量（需手动创建）
│   ├── .env.example           # 环境变量模板
│   ├── .gitignore             # Git 忽略规则
│   ├── requirements.txt       # Python 依赖
│   └── README.md              # 项目说明
│
├── 🚀 启动脚本
│   ├── install.ps1            # 依赖安装脚本（PowerShell）
│   ├── start.ps1              # 快速启动脚本（PowerShell）
│   └── test_setup.py          # 环境测试脚本
│
└── 📁 输出目录
    ├── reports/               # 生成的报告（.md 文件）
    └── cache/                 # 缓存数据
```

## 🔄 数据流

```
用户输入（导师姓名）
    ↓
┌─────────────────────────────────────┐
│  DataCollectorAgent                 │
│  - Google Scholar 搜索              │
│  - arXiv 搜索                       │
│  - 合并去重                         │
└─────────────────────────────────────┘
    ↓ (论文列表)
┌─────────────────────────────────────┐
│  ResearchAnalyzerAgent (GPT-4)      │
│  - 识别研究方向                     │
│  - 总结关键贡献                     │
│  - 分析领域问题                     │
└─────────────────────────────────────┘
    ↓ (分析结果)
┌─────────────────────────────────────┐
│  MentorAgent (GPT-4)                │
│  - 设计本科生任务                   │
│  - 循序渐进规划                     │
└─────────────────────────────────────┘
    ↓ (任务列表)
┌─────────────────────────────────────┐
│  ReportGenerator                    │
│  - 格式化为 Markdown                │
│  - 保存到文件                       │
└─────────────────────────────────────┘
    ↓
最终报告（.md 文件）
```

## 🎯 核心组件说明

### 1. 数据层（Scrapers）

**scholar_scraper.py**
- 使用 `scholarly` 库访问 Google Scholar
- 获取导师基本信息、研究兴趣
- 抓取近期论文及引用数
- 支持失败重试机制

**arxiv_scraper.py**
- 使用官方 `arxiv` API
- 搜索预印本论文
- 支持按作者、关键词搜索
- 获取完整摘要

### 2. 逻辑层（Agents）

**data_collector.py**
- 协调两个爬虫
- 论文去重（基于标题）
- 按年份和引用数排序

**research_analyzer.py** ⭐
- 调用 GPT-4 深度分析
- 识别 3-5 个研究方向
- 总结代表性贡献
- 分析领域核心问题

**mentor_agent.py** ⭐
- 设计本科生科研任务
- 文献综述、代码复现、数据分析
- 难度递增、具体可执行

### 3. 工作流（Workflow）

**workflow.py**
- 使用 LangGraph 构建
- 自动状态管理
- 节点间数据传递
- 支持命令行调用

### 4. 表现层

**app.py**
- Streamlit Web 界面
- 实时进度显示
- 报告预览和下载
- 配置检查

## 🔑 关键技术

| 技术 | 用途 | 备选方案 |
|------|------|----------|
| LangGraph | 多代理协作 | LangChain Agents, CrewAI |
| OpenAI GPT-4 | 深度分析 | Claude, Gemini, 本地 Llama |
| scholarly | Google Scholar | 手写爬虫 + BeautifulSoup |
| arxiv API | 预印本搜索 | 无（官方 API） |
| Streamlit | Web 界面 | Gradio, Flask+React |

## 💡 设计思路

### 为什么用 LangGraph？
- **状态管理**: 自动处理 Agent 间的数据传递
- **可扩展**: 轻松添加新 Agent（如论文下载器）
- **可视化**: 可以画出工作流图
- **错误处理**: 内置重试和错误恢复

### 为什么用 GPT-4？
- **理解力强**: 能准确把握研究方向
- **生成质量高**: 输出连贯、专业
- **领域知识**: 预训练包含大量学术文献
- **创造性**: 能设计有价值的科研任务

### 成本优化策略
1. **缓存**: 避免重复分析同一导师
2. **批处理**: 一次性传递多篇论文摘要
3. **温度控制**: 降低 temperature 减少 token 消耗
4. **选择性分析**: 只深度分析高被引论文

## 🚧 扩展方向

### 短期（1-2周）
- [ ] 添加导师对比功能
- [ ] 支持中文导师名
- [ ] 生成 PDF 报告
- [ ] 添加错误恢复

### 中期（1个月）
- [ ] 构建导师数据库
- [ ] 支持 Web of Science
- [ ] 添加校园网代理
- [ ] 实现报告评分

### 长期（2-3个月）
- [ ] 多语言支持
- [ ] 推荐系统（匹配学生兴趣）
- [ ] 可视化研究网络
- [ ] 社区反馈系统

## 📊 预期性能

| 指标 | 数值 |
|------|------|
| 单次分析时间 | 2-5 分钟 |
| 论文收集数量 | 10-30 篇 |
| 报告长度 | 2000-3000 字 |
| API 调用成本 | $0.2-$1.0 |
| 成功率 | >90% |

## 🎓 使用场景

1. **本研选导师**
   - 快速了解多位导师
   - 对比研究方向
   - 确定感兴趣的课题

2. **科研入门**
   - 获得具体学习路径
   - 了解领域核心问题
   - 准备与导师面谈

3. **转方向准备**
   - 探索新领域
   - 评估难度和兴趣
   - 规划学习计划
