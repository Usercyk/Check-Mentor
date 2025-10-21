"""
处理王剑威老师的论文
自动扫描 Downloads_md/王剑威/ 目录下的所有论文并进行分析
"""
from pathlib import Path
from datetime import datetime
from rag_processor import PaperRAGProcessor
from data_manager import DataManager
import config


def scan_papers_directory(base_dir: Path) -> list:
    """
    扫描论文目录，生成论文信息列表
    
    Args:
        base_dir: 基础目录路径（如 Downloads_md/王剑威）
        
    Returns:
        论文信息列表
    """
    papers_info = []
    paper_id = 1
    
    # 扫描三个分类目录
    for category in ['main', 'ref1', 'ref2']:
        category_dir = base_dir / category
        
        if not category_dir.exists():
            print(f"⚠️  Directory not found: {category_dir}")
            continue
        
        print(f"📁 Scanning {category} directory...")
        
        # 获取所有 .md 文件
        md_files = list(category_dir.glob('*.md'))
        print(f"   Found {len(md_files)} papers")
        
        for md_file in md_files:
            # 从文件名提取标题（去掉 .md 后缀）
            title = md_file.stem
            
            paper_info = {
                'id': f"paper_{paper_id:03d}",
                'title': title,
                'category': category,
                'md_filename': md_file.name,
                'file_path': str(md_file),
                # 以下信息需要从论文内容中提取，这里先用占位符
                'authors': [],
                'year': None,
            }
            
            papers_info.append(paper_info)
            paper_id += 1
    
    return papers_info


def main():
    """主函数"""
    print(f"\n{'='*70}")
    print(f"🎓 {config.PROJECT_NAME} - 王剑威老师论文分析")
    print(f"{'='*70}\n")
    
    # 初始化数据管理器
    output_file = "wang_jianwei_research_data.json"
    data_manager = DataManager(output_file)
    
    # 设置教授信息
    print("📝 Setting professor information...")
    data_manager.set_professor_info(
        name="王剑威",
        department="物理学院",
        university="北京大学",
        research_areas=["量子计算", "光子学", "量子纠缠", "硅光子芯片"],
        position="副教授"
    )
    
    # 扫描论文目录
    base_dir = Path("Downloads_md/王剑威")
    
    if not base_dir.exists():
        print(f"❌ Error: Directory not found: {base_dir}")
        print(f"Please ensure the papers are in the correct location.")
        return
    
    print(f"\n📚 Scanning papers from: {base_dir}")
    papers_info = scan_papers_directory(base_dir)
    
    if not papers_info:
        print("❌ No papers found!")
        return
    
    # 统计信息
    main_count = sum(1 for p in papers_info if p['category'] == 'main')
    ref1_count = sum(1 for p in papers_info if p['category'] == 'ref1')
    ref2_count = sum(1 for p in papers_info if p['category'] == 'ref2')
    
    print(f"\n📊 Paper Statistics:")
    print(f"   Main papers (主要论文): {main_count}")
    print(f"   Ref1 papers (一级引用): {ref1_count}")
    print(f"   Ref2 papers (二级引用): {ref2_count}")
    print(f"   Total: {len(papers_info)} papers")
    
    # 添加论文到数据管理器
    print(f"\n💾 Adding papers to database...")
    for paper_info in papers_info:
        data_manager.add_paper(paper_info)
    
    # 添加数据源信息
    data_manager.add_data_source("Downloads_md/王剑威")
    data_manager.update_metadata(
        analysis_date=datetime.now().isoformat(),
        total_papers=len(papers_info)
    )
    
    # 保存初始数据
    data_manager.save()
    print(f"✓ Initial data saved to: {data_manager.data_file}")
    
    # 询问是否继续处理
    print(f"\n{'='*70}")
    print(f"📋 Next Steps:")
    print(f"{'='*70}")
    print(f"1. Papers have been cataloged")
    print(f"2. Ready to start RAG processing")
    print(f"\nThis will:")
    print(f"   - Load and chunk all {len(papers_info)} papers")
    print(f"   - Create vector embeddings (using OpenAI API)")
    print(f"   - Generate summaries for each paper")
    print(f"   - Analyze relevance across 5 dimensions")
    print(f"\n⚠️  Warning: This will consume API credits and may take some time.")
    
    response = input(f"\nProceed with full analysis? (yes/no): ").strip().lower()
    
    if response not in ['yes', 'y']:
        print(f"\n✓ Setup complete. Run this script again to start analysis.")
        return
    
    # 初始化 RAG 处理器
    print(f"\n{'='*70}")
    print(f"🚀 Starting RAG Processing")
    print(f"{'='*70}\n")
    
    processor = PaperRAGProcessor()
    
    # 批量处理论文
    # 注意：这里我们使用 Downloads_md/王剑威 作为基础目录
    # 但实际上我们需要处理三个子目录
    
    # 方案：分别处理每个类别，但使用同一个向量库
    all_results = {
        "summaries": {},
        "analysis_results": {}
    }
    
    for category in ['main', 'ref1', 'ref2']:
        category_papers = [p for p in papers_info if p['category'] == category]
        
        if not category_papers:
            continue
        
        print(f"\n{'='*70}")
        print(f"📂 Processing {category} papers ({len(category_papers)} papers)")
        print(f"{'='*70}\n")
        
        category_dir = str(base_dir / category)
        
        try:
            results = processor.process_papers_batch(
                category_papers, 
                category_dir,
                file_type="md"
            )
            
            # 合并结果
            all_results["summaries"].update(results["summaries"])
            all_results["analysis_results"].update(results["analysis_results"])
            
        except Exception as e:
            print(f"❌ Error processing {category}: {e}")
            import traceback
            traceback.print_exc()
            continue
    
    # 保存所有结果
    print(f"\n{'='*70}")
    print(f"💾 Saving results")
    print(f"{'='*70}\n")
    
    # 保存总结
    for paper_id, summary in all_results["summaries"].items():
        data_manager.add_paper_summary(paper_id, summary)
    
    # 保存分析结果
    for paper_id, analysis in all_results["analysis_results"].items():
        data_manager.add_analysis_result(paper_id, analysis)
    
    # 最终保存
    data_manager.save()
    
    # 导出摘要
    summary_file = config.OUTPUT_DIR / "wang_jianwei_analysis_summary.md"
    summary_text = data_manager.export_analysis_summary(str(summary_file))
    
    print(f"\n{'='*70}")
    print(f"✅ Processing Complete!")
    print(f"{'='*70}")
    print(f"\nResults saved to:")
    print(f"  - Data file: {data_manager.data_file}")
    print(f"  - Vector store: {processor.persist_directory}")
    print(f"  - Summary: {summary_file}")
    print(f"\nTotal papers processed: {len(papers_info)}")
    print(f"  - Summaries generated: {len(all_results['summaries'])}")
    print(f"  - Analyses completed: {len(all_results['analysis_results'])}")


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
    except KeyboardInterrupt:
        print(f"\n\n⚠️  Process interrupted by user.")
    except Exception as e:
        print(f"\n❌ Error:")
        print(f"{e}")
        import traceback
        traceback.print_exc()
