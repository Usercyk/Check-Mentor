"""
主程序示例
展示如何使用 RAG 处理器完成任务 1-5
"""
from datetime import datetime
from rag_processor import PaperRAGProcessor
from data_manager import DataManager
import config


def main():
    """主函数"""
    print(f"\n{'='*70}")
    print(f"🎓 {config.PROJECT_NAME} - Paper Analysis System")
    print(f"{'='*70}\n")
    
    # 初始化数据管理器 - 使用教授名字作为文件名
    professor_name = "王剑威"
    data_file = f"{professor_name}_research_data.json"
    data_manager = DataManager(data_file)
    
    # 设置教授信息
    data_manager.set_professor_info(
        name=professor_name,
        department="物理系",
        university="清华大学",
        research_areas=["量子计算", "量子信息", "量子光学", "集成光子学"]
    )
    
    # 自动扫描 Downloads_md 中的论文（使用小样本以节省API调用）
    from pathlib import Path
    downloads_dir = config.BASE_DIR / "Downloads_md" / professor_name
    
    papers_info = []
    paper_id_counter = 1
    
    # 设置每个文件夹的采样数量（为了节省API调用）- 只处理两篇论文进行测试
    sample_sizes = {
        "main": 1,  # main文件夹处理1个文件
        "ref1": 1,  # ref1文件夹处理1个文件
        "ref2": 0   # ref2文件夹不处理
    }
    
    # 扫描所有子文件夹
    for subfolder in downloads_dir.iterdir():
        if subfolder.is_dir():
            folder_name = subfolder.name  # main, ref1, ref2等
            sample_size = sample_sizes.get(folder_name, 1)  # 默认1个
            
            # 获取该文件夹下的所有md文件
            md_files = list(subfolder.glob("**/*.md"))
            
            # 只处理指定数量的文件
            selected_files = md_files[:sample_size]
            
            print(f"📁 Processing folder '{folder_name}': {len(selected_files)}/{len(md_files)} files")
            
            for md_file in selected_files:
                # 从文件名生成标题（去掉.md扩展名）
                title = md_file.stem
                
                # 生成唯一ID
                paper_id = f"{paper_id_counter:03d}"
                
                paper_info = {
                    "id": paper_id,
                    "title": title,
                    "authors": [professor_name],  # 主要作者为教授
                    "year": 2024,  # 默认年份，可根据需要调整
                    "md_filename": str(md_file.relative_to(downloads_dir)),
                    "category": folder_name  # 添加类别信息
                }
                
                papers_info.append(paper_info)
                paper_id_counter += 1
    
    # 添加论文到数据管理器
    for paper_info in papers_info:
        data_manager.add_paper(paper_info)
    
    # 更新元数据
    data_manager.add_data_source("王剑威论文集")
    data_manager.update_metadata(
        analysis_date=datetime.now().isoformat()
    )
    
    # 初始化 RAG 处理器
    processor = PaperRAGProcessor()
    
    # 设置文件目录和文件类型
    # 支持 "pdf" 或 "md" (markdown) 格式
    file_type = "md"  # 改为 "pdf" 如果使用 PDF 文件
    
    if file_type == "md":
        paper_directory = downloads_dir  # Markdown 文件目录
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
    
    print(f"\n{'='*70}")
    print(f"✅ Processing complete!")
    print(f"{'='*70}")
    print(f"\nResults saved to:")
    print(f"  - Data file: {data_manager.data_file}")
    print(f"  - Vector store: {processor.persist_directory}")


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
