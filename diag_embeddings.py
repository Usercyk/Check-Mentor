"""
诊断脚本：检查 embeddings 输入类型和示例内容
"""
from dotenv import load_dotenv
from rag_processor import PaperRAGProcessor
from pathlib import Path

load_dotenv()


def run_diag(papers_root: str = 'Downloads_md/王剑威/main', sample_index: int = 0):
    """运行诊断：加载第一个 Markdown 文件并尝试生成 embeddings（不会在导入时执行）。"""
    processor = PaperRAGProcessor()

    papers_dir = Path(papers_root)
    files = list(papers_dir.glob('*.md'))
    if not files:
        raise FileNotFoundError(f'No markdown papers found in {papers_dir}')

    sample_file = str(files[sample_index])

    # 加载单篇论文的文档
    paper_meta = {'id': 'diag_sample', 'title': files[sample_index].stem}
    docs = processor.load_single_paper(sample_file, paper_meta)
    # loaded docs count available for callers

    # Prepare cleaned texts
    texts = []
    for d in docs:
        if hasattr(d, 'page_content') and isinstance(d.page_content, str):
            content = d.page_content.replace('\x00', '').strip()
            if content:
                texts.append(content)
        else:
            texts.append(str(d.page_content))

    # Try embedding small batch
    emb = processor.embeddings.embed_documents(texts[:16])
    result = {
        'sample_file': sample_file,
        'num_docs': len(docs),
        'num_texts': len(texts),
        'vectors_count': len(emb),
        'vector_dim': len(emb[0]) if emb else 0,
    }
    return result


if __name__ == '__main__':
    try:
        run_diag()
    except Exception as e:
        print('Diag error:', repr(e))
