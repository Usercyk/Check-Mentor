# 🚀 快速开始指南

## 步骤 1: 安装依赖

### 方法 A: 使用安装脚本（推荐）

```powershell
# 在 PowerShell 中运行
.\install.ps1
```

这个脚本会自动：
- ✅ 创建虚拟环境
- ✅ 安装所有依赖
- ✅ 创建 .env 文件

### 方法 B: 手动安装

```powershell
# 1. 创建虚拟环境
python -m venv venv

# 2. 激活虚拟环境
.\venv\Scripts\Activate.ps1

# 3. 升级 pip
python -m pip install --upgrade pip

# 4. 安装依赖
pip install -r requirements.txt
```

## 步骤 2: 配置 API Key

### 2.1 获取 OpenAI API Key

访问 [OpenAI Platform](https://platform.openai.com/api-keys) 并：
1. 注册/登录账号
2. 点击 "Create new secret key"
3. 复制 API Key（以 `sk-` 开头）

💡 **国内用户提示**：
- 可以使用国内的 OpenAI API 代理服务
- 或者使用兼容 OpenAI 接口的其他服务（如通义千问、智谱 AI 等）

### 2.2 配置环境变量

```powershell
# 复制模板文件
copy .env.example .env

# 编辑 .env 文件
notepad .env
```

在 `.env` 文件中填入：
```env
OPENAI_API_KEY=sk-your-actual-api-key-here
LLM_MODEL=gpt-4-turbo-preview
```

## 步骤 3: 测试环境

```powershell
python test_setup.py
```

如果看到 "🎉 所有测试通过!"，说明环境配置成功！

## 步骤 4: 开始使用

### 方法 A: Web 界面（推荐）⭐

```powershell
# 启动 Web 应用
streamlit run app.py
```

然后在浏览器中访问 `http://localhost:8501`

**操作步骤**：
1. 输入导师的英文姓名（如 `Zhang Wei`）
2. 点击 "🚀 开始分析"
3. 等待 2-5 分钟
4. 查看和下载生成的报告

### 方法 B: 快速启动脚本

```powershell
.\start.ps1
```

这个脚本提供交互式菜单：
- 选项 1: 启动 Web 界面
- 选项 2: 命令行模式
- 选项 3: 退出

### 方法 C: 命令行

```powershell
# 直接运行
python main.py "Zhang Wei"

# 或者交互式输入
python main.py
```

报告会保存在 `reports/` 目录。

---

## 📖 详细使用示例

### 示例 1: 分析单个导师

```powershell
# 激活环境
.\venv\Scripts\Activate.ps1

# 分析导师
python main.py "Qi-Kun Xue"
```

**预期输出**：
```
============================================================
🎓 学术开盒 (Check-Mentor)
为物理学本科生准备的导师研究分析工具
============================================================

🎯 开始为 Qi-Kun Xue 教授生成学术档案
============================================================

============================================================
📊 数据收集代理开始工作...
============================================================

🔍 正在 Google Scholar 搜索: Qi-Kun Xue
✅ 找到导师: Qi-Kun Xue - Tsinghua University
📚 正在获取 Qi-Kun Xue 的近期论文...
  ✓ Observation of the quantum anomalous Hall effect... (2023)
  ✓ Superconductivity in topological materials... (2022)
  ...

🔍 正在 arXiv 搜索: Qi-Kun Xue
  ✓ Quantum transport in topological insulators... (2023)
  ...

============================================================
🔬 研究分析代理开始工作...
============================================================

📍 分析研究方向...
  ✓ 识别出 4 个研究方向
    • 拓扑量子材料: 研究新型拓扑绝缘体和拓扑超导体
    • 量子反常霍尔效应: 探索零磁场下的量子化输运
    ...

============================================================
✨ 工作流完成！
============================================================

✅ 报告已生成: reports/Qi-Kun_Xue_20251011.md
📊 共分析 25 篇论文
```

### 示例 2: 使用 Web 界面

1. **启动应用**
   ```powershell
   streamlit run app.py
   ```

2. **在浏览器中操作**
   - URL: `http://localhost:8501`
   - 输入: `Zhang Wei`
   - 点击: "🚀 开始分析"

3. **查看结果**
   - 实时进度条显示
   - 统计信息卡片
   - Markdown 报告预览
   - 下载按钮

### 示例 3: 批量分析多个导师

创建一个批处理脚本 `batch_analyze.py`:

```python
from workflow import ResearchWorkflow

professors = [
    "Zhang Wei",
    "Li Ming", 
    "Wang Fang"
]

workflow = ResearchWorkflow()

for prof in professors:
    print(f"\n正在分析: {prof}")
    try:
        result = workflow.run(prof)
        print(f"✅ 完成: {prof}")
    except Exception as e:
        print(f"❌ 失败: {prof} - {e}")
```

运行：
```powershell
python batch_analyze.py
```

---

## 🎯 生成报告解读

生成的报告包含 5 个部分：

### 1️⃣ 基本信息
- 导师姓名、机构、主页
- 研究兴趣关键词
- 分析的论文数量

### 2️⃣ 近期研究方向
- 3-5 个主要方向
- 每个方向的简洁描述
- 基于论文频率和时效性

### 3️⃣ 代表性学术贡献
- 高被引论文分析
- 关键创新点总结
- 学术影响力评估

### 4️⃣ 领域核心问题
- 研究领域的宏观问题
- 当前技术挑战
- 潜在应用价值

### 5️⃣ 本科生科研任务 ⭐
- **任务 1**: 文献综述（入门）
- **任务 2**: 经典复现（进阶）
- **任务 3**: 数据分析（应用）
- **任务 4**: 理论推导（深入）

每个任务包含：
- 具体描述
- 预期成果
- 预计时间

---

## ⚙️ 高级配置

### 调整分析参数

编辑 `config.py`:

```python
# 每个来源最多获取的论文数
MAX_PAPERS_PER_SOURCE = 15  # 默认 10

# 分析最近几年的论文
RECENT_YEARS = 3  # 默认 5

# LLM 温度（越低越严谨）
TEMPERATURE = 0.2  # 默认 0.3
```

### 使用不同的 LLM

**选项 1: GPT-3.5（成本更低）**
```env
LLM_MODEL=gpt-3.5-turbo
```

**选项 2: Claude（通过代理）**
```env
OPENAI_API_BASE=https://your-claude-proxy.com/v1
OPENAI_API_KEY=your-claude-key
```

**选项 3: 国内大模型**
```env
# 通义千问
OPENAI_API_BASE=https://dashscope.aliyuncs.com/compatible-mode/v1
OPENAI_API_KEY=sk-your-qwen-key

# 智谱 AI
OPENAI_API_BASE=https://open.bigmodel.cn/api/paas/v4/
OPENAI_API_KEY=your-zhipu-key
```

### 启用 Google Scholar 代理

编辑 `scrapers/scholar_scraper.py`:

```python
def __init__(self):
    # 启用代理
    pg = ProxyGenerator()
    pg.FreeProxies()  # 或 pg.ScraperAPI("your-api-key")
    scholarly.use_proxy(pg)
```

---

## 🐛 常见问题

### Q1: "无法解析导入" 错误

**原因**: 依赖未安装或虚拟环境未激活

**解决**:
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Q2: "未找到导师" 

**原因**: 
- 姓名拼写错误
- 导师没有 Google Scholar 主页
- 网络问题

**解决**:
1. 检查姓名拼写（使用导师论文上的英文名）
2. 尝试姓名的不同变体
3. 检查网络连接

### Q3: API 调用失败

**原因**: 
- API Key 错误
- 余额不足
- 网络问题

**解决**:
1. 检查 `.env` 中的 `OPENAI_API_KEY`
2. 访问 [OpenAI Platform](https://platform.openai.com/account/usage) 检查余额
3. 检查是否需要代理

### Q4: Google Scholar 被封禁

**原因**: 请求过于频繁

**解决**:
1. 降低 `MAX_PAPERS_PER_SOURCE`
2. 增加请求间隔（修改 `scholar_scraper.py` 中的 `time.sleep()`）
3. 启用代理

### Q5: 报告质量不佳

**解决**:
1. 使用 GPT-4 而非 GPT-3.5
2. 增加 `MAX_PAPERS_PER_SOURCE`
3. 降低 `TEMPERATURE` 参数

---

## 💰 成本估算

| 模型 | 单次成本 | 月度成本（30次） |
|------|----------|-----------------|
| GPT-4 Turbo | $0.50 - $1.00 | $15 - $30 |
| GPT-3.5 Turbo | $0.10 - $0.20 | $3 - $6 |
| Claude 3 | $0.40 - $0.80 | $12 - $24 |

💡 **节省成本的方法**:
1. 先用 GPT-3.5 测试，确定需要后再用 GPT-4
2. 开启缓存，避免重复分析
3. 批量分析多个导师

---

## 📚 下一步

✅ 环境配置完成后：

1. **阅读生成的报告**: 了解报告结构
2. **尝试不同导师**: 测试不同领域
3. **调整参数**: 优化分析质量
4. **定制化修改**: 根据需求修改代码

🎯 **建议工作流**:
1. 列出感兴趣的 5-10 位导师
2. 批量生成报告
3. 对比分析，筛选 2-3 位
4. 深入阅读他们的代表作
5. 准备问题，联系导师

---

**祝你找到理想的导师，开启精彩的科研之旅！🌟**
