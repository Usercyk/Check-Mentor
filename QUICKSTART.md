# 快速开始指南

## 第一步：安装依赖

```powershell
pip install -r requirements.txt
```

## 第二步：配置 API 密钥

1. 复制配置模板：
```powershell
cp .env.example .env
```

2. 编辑 `.env` 文件，填入你的 OpenAI API 密钥：
```
OPENAI_API_KEY=sk-your-api-key-here
```

## 第三步：准备 PDF 文件

创建数据目录并放入 PDF 文件：
```powershell
# 创建目录
mkdir data\pdfs

# 将你的 PDF 论文复制到 data\pdfs\ 目录
```

## 第四步：运行程序

```powershell
python main.py
```

## 查看结果

程序会生成以下文件：
- `professor_research_data.json` - 完整的分析结果
- `output/analysis_summary.md` - 可读的分析摘要
- `chroma_db/` - 向量数据库（用于后续查询）

## 常见问题

### Q: 运行时提示 API 密钥错误？
A: 检查 `.env` 文件是否正确配置了 `OPENAI_API_KEY`

### Q: 找不到 PDF 文件？
A: 确保 PDF 文件放在 `data/pdfs/` 目录下

### Q: 内存不足？
A: 减少一次处理的 PDF 文件数量，或增加系统内存

### Q: API 调用太慢？
A: OpenAI API 响应时间取决于网络和服务器负载，请耐心等待

## 自定义配置

在 `main.py` 中可以修改：
- PDF 目录路径
- 教授信息
- 论文信息列表

在 `.env` 中可以修改：
- API 密钥
- 使用的模型
- 块大小和重叠设置
