# 使用 Markdown 格式论文的说明

## ✅ 已完成的配置

1. ✅ 已安装所有依赖（包括 unstructured, markdown）
2. ✅ 代码已支持 PDF 和 Markdown 两种格式
3. ✅ 已创建示例 Markdown 论文：`data/papers/example_paper.md`
4. ✅ `main.py` 已配置为使用 Markdown 格式（`file_type = "md"`）

## 📝 如何准备你的 Markdown 论文

### 方法 1：直接使用 Markdown 文件
如果你已经有 Markdown 格式的论文，直接复制到 `data/papers/` 目录：

```powershell
# 复制你的 Markdown 文件
cp 你的论文路径/*.md data/papers/
```

### 方法 2：从 PDF 转换为 Markdown
如果你的论文是 PDF 格式，可以使用工具转换：

**推荐工具：**
- **Mathpix**: https://mathpix.com/ （支持公式识别）
- **Marker**: https://github.com/VikParuchuri/marker （开源，效果好）
- **PyPDF + GPT**: 提取文本后用 GPT 整理格式

**使用 Marker 转换示例：**
```powershell
# 安装 marker
pip install marker-pdf

# 转换 PDF 到 Markdown
marker_single your_paper.pdf data/papers/ --batch_multiplier 2
```

### 方法 3：直接粘贴文本
1. 打开 PDF 论文
2. 复制文本内容
3. 新建 `.md` 文件并粘贴
4. 简单整理格式（添加标题、段落等）

## 📋 Markdown 论文的推荐格式

```markdown
# 论文标题

## Authors
作者1, 作者2, 作者3

## Abstract
摘要内容...

## 1. Introduction
引言内容...

### 1.1 Background
背景信息...

## 2. Methods
方法描述...

## 3. Results
实验结果...

## 4. Discussion
讨论...

## 5. Conclusion
结论...

## References
1. 参考文献1
2. 参考文献2
```

## 🚀 运行示例

现在你可以直接运行系统测试：

```powershell
python main.py
```

系统会：
1. 加载 `data/papers/` 目录中的所有 `.md` 文件
2. 分割文本为块
3. 创建向量嵌入
4. 分析与教授研究的相关性
5. 生成分析报告

## ⚙️ 切换回 PDF 格式

如果你想使用 PDF 格式，编辑 `main.py` 的第 63 行：

```python
# 改为 PDF
file_type = "pdf"  # 改回这个值

# 相应的，PDF 文件应该放在 data/pdfs/ 目录
```

## 📊 查看结果

运行完成后，查看：
- `professor_research_data.json` - 完整的分析数据
- `output/analysis_summary.md` - 易读的分析摘要
- `chroma_db/` - 向量数据库（用于后续查询）

## 💡 提示

1. **Markdown 格式的优势**：
   - 易于编辑和修改
   - 文本提取更准确
   - 没有 PDF 解析的错误
   - 可以添加注释和标记

2. **论文元数据**：
   在 `main.py` 中更新论文信息：
   ```python
   papers_info = [
       {
           "id": "paper_001",
           "title": "你的论文标题",
           "authors": ["作者1", "作者2"],
           "year": 2024,
           "md_filename": "your_paper.md"  # 使用 md_filename
       }
   ]
   ```

3. **批量处理**：
   - 把所有 Markdown 文件放在 `data/papers/` 目录
   - 在 `papers_info` 列表中添加所有论文的元数据
   - 运行一次处理所有论文

## 🔧 故障排除

### 问题：找不到论文文件
**解决**：检查文件路径和 `papers_info` 中的 `md_filename` 是否匹配

### 问题：API 调用失败
**解决**：检查 `.env` 文件中的 `OPENAI_API_KEY` 是否正确配置

### 问题：内存不足
**解决**：减少一次处理的论文数量，或调整 `CHUNK_SIZE` 参数

## 📚 参考资源

- [LangChain 文档](https://python.langchain.com/)
- [Chroma 向量数据库](https://www.trychroma.com/)
- [OpenAI API 文档](https://platform.openai.com/docs)
