"""
诊断脚本：检查 embeddings 输入类型和示例内容
"""
import os
from dotenv import load_dotenv
from rag_processor import PaperRAGProcessor
from pathlib import Path

load_dotenv()

processor = PaperRAGProcessor()

# 找到王剑威论文目录，取第一个文件
papers_dir = Path('Downloads_md') / '王剑威' / 'main'
files = list(papers_dir.glob('*.md'))
if not files:
    print('No markdown papers found in', papers_dir)
    raise SystemExit(1)

sample_file = str(files[0])
print('Sample file:', sample_file)

# 加载单篇论文的文档
paper_meta = {'id': 'diag_sample', 'title': files[0].stem}
docs = processor.load_single_paper(sample_file, paper_meta)
print('Loaded docs:', len(docs))

# 查看前几个 doc 的类型与内容摘要
for i, d in enumerate(docs[:10]):
    print(f'-- doc {i} type: {type(d)}; page_content type: {type(d.page_content)}; len:',
          len(d.page_content) if isinstance(d.page_content, str) else 'N/A')
    # print a small snippet
    snippet = d.page_content[:200] if isinstance(d.page_content, str) else repr(d.page_content)[:200]
    print('   snippet:', repr(snippet))

# Prepare cleaned texts
texts = []
for d in docs:
    if hasattr(d, 'page_content') and isinstance(d.page_content, str):
        content = d.page_content.replace('\x00', '').strip()
        if content:
            texts.append(content)
    else:
        texts.append(str(d.page_content))

print('Prepared texts:', len(texts))

# Try embedding small batch
try:
    emb = processor.embeddings.embed_documents(texts[:16])
    print('Embedding succeeded, got', len(emb), 'vectors')
    print('First dim:', len(emb[0]))
except Exception as e:
    print('Embedding error:', repr(e))
    # Print problematic item types
    for i, t in enumerate(texts[:16]):
        print(i, type(t), isinstance(t, str), (len(t) if isinstance(t, str) else 'N/A'))
    raise
