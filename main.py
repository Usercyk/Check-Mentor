"""
主程序示例
展示如何使用 RAG 处理器完成任务 1-5
"""
from pathlib import Path
from datetime import datetime
from rag_processor import PaperRAGProcessor
from data_manager import DataManager
import config


def main():
    """主函数"""
    print(f"\n{'='*70}")
    print(f"🎓 {config.PROJECT_NAME} - Paper Analysis System")
    print(f"{'='*70}\n")
    
    # 初始化数据管理器
    data_manager = DataManager("professor_research_data.json")
    
    # 设置教授信息（示例）
    data_manager.set_professor_info(
        name="示例教授",
        department="物理系",
        university="示例大学",
        research_areas=["量子计算", "凝聚态物理"]
    )
    
    # 准备论文信息列表（示例）
    # 实际使用时，这些信息应该从爬虫或其他数据源获取
    papers_info = [
        {
            "id": "paper_001",
            "title": "Quantum Computing Advances",
            "authors": ["Alice Smith", "Bob Johnson"],
            "year": 2024,
            "pdf_filename": "paper_001.pdf"
        },
        {
            "id": "paper_002", 
            "title": "Condensed Matter Physics Study",
            "authors": ["Charlie Brown"],
            "year": 2023,
            "pdf_filename": "paper_002.pdf"
        }
        # 添加更多论文...
    ]
    
    # 添加论文到数据管理器
    for paper_info in papers_info:
        data_manager.add_paper(paper_info)
    
    # 更新元数据
    data_manager.add_data_source("arXiv")
    data_manager.update_metadata(
        analysis_date=datetime.now().isoformat()
    )
    
    # 初始化 RAG 处理器
    processor = PaperRAGProcessor()
    
    # 设置文件目录和文件类型
    # 支持 "pdf" 或 "md" (markdown) 格式
    file_type = "md"  # 改为 "pdf" 如果使用 PDF 文件
    
    if file_type == "md":
        paper_directory = config.DATA_DIR / "papers"  # Markdown 文件目录
    else:
        paper_directory = config.DATA_DIR / "pdfs"  # PDF 文件目录
    
    # 检查目录是否存在
    if not paper_directory.exists():
        print(f"⚠️  Paper directory not found: {paper_directory}")
        print(f"Please create the directory and add {file_type.upper()} files, or update the path in main.py")
        
        # 创建示例目录
        paper_directory.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {paper_directory}")
        print(f"\nPlease add {file_type.upper()} files to this directory and run again.")
        return
    
    # 批量处理论文
    print(f"\n📚 Processing {len(papers_info)} papers...")
    print(f"Paper directory: {paper_directory}")
    print(f"File type: {file_type.upper()}\n")
    
    results = processor.process_papers_batch(papers_info, str(paper_directory), file_type=file_type)
    
    # 保存结果到数据管理器
    print(f"\n💾 Saving results...")
    
    # 保存总结
    for paper_id, summary in results["summaries"].items():
        data_manager.add_paper_summary(paper_id, summary)
    
    # 保存分析结果
    for paper_id, analysis in results["analysis_results"].items():
        data_manager.add_analysis_result(paper_id, analysis)
    
    # 保存到文件
    data_manager.save()
    
    # 导出摘要
    summary_text = data_manager.export_analysis_summary("analysis_summary.md")
    print(f"\n" + "="*70)
    print(f"📊 Analysis Summary:")
    print(f"="*70)
    print(summary_text[:500] + "..." if len(summary_text) > 500 else summary_text)
    
    print(f"\n{'='*70}")
    print(f"✅ Processing complete!")
    print(f"{'='*70}")
    print(f"\nResults saved to:")
    print(f"  - Data file: {data_manager.data_file}")
    print(f"  - Vector store: {processor.persist_directory}")
    print(f"  - Summary: {config.OUTPUT_DIR / 'analysis_summary.md'}")


if __name__ == "__main__":
    try:
        # 验证配置
        config.validate_config()
        
        # 运行主程序
        main()
        
    except ValueError as e:
        print(f"\n❌ Configuration Error:")
        print(f"{e}")
        print(f"\nPlease check your .env file and ensure all required API keys are set.")
    except Exception as e:
        print(f"\n❌ Error:")
        print(f"{e}")
        import traceback
        traceback.print_exc()
