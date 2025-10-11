"""
快速测试脚本 - 测试各个模块是否正常工作
"""
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent))


def test_imports():
    """测试所有导入是否正常"""
    print("📦 测试模块导入...")
    
    try:
        import config
        print("  ✓ config")
        
        from scrapers import Paper, ProfessorProfile
        print("  ✓ scrapers")
        
        from scrapers.scholar_scraper import ScholarScraper
        print("  ✓ scholar_scraper")
        
        from scrapers.arxiv_scraper import ArxivScraper
        print("  ✓ arxiv_scraper")
        
        from agents import AgentState
        print("  ✓ agents")
        
        from agents.data_collector import DataCollectorAgent
        print("  ✓ data_collector")
        
        from agents.research_analyzer import ResearchAnalyzerAgent
        print("  ✓ research_analyzer")
        
        from agents.mentor_agent import MentorAgent
        print("  ✓ mentor_agent")
        
        from report_generator import ReportGenerator
        print("  ✓ report_generator")
        
        from workflow import ResearchWorkflow
        print("  ✓ workflow")
        
        print("\n✅ 所有模块导入成功!\n")
        return True
        
    except ImportError as e:
        print(f"\n❌ 导入失败: {e}\n")
        print("💡 请运行: pip install -r requirements.txt")
        return False


def test_config():
    """测试配置"""
    print("⚙️ 测试配置...")
    
    import config
    
    print(f"  • OpenAI API Key: {'已设置' if config.OPENAI_API_KEY else '❌ 未设置'}")
    print(f"  • LLM Model: {config.LLM_MODEL}")
    print(f"  • Max Papers: {config.MAX_PAPERS_PER_SOURCE}")
    print(f"  • Recent Years: {config.RECENT_YEARS}")
    print(f"  • Reports Dir: {config.REPORTS_DIR}")
    
    if not config.OPENAI_API_KEY:
        print("\n⚠️ 警告: 未设置 OPENAI_API_KEY")
        print("  请在 .env 文件中配置")
        return False
    
    print("\n✅ 配置检查通过!\n")
    return True


def test_scrapers():
    """测试爬虫（简单测试，不实际爬取）"""
    print("🔍 测试爬虫模块...")
    
    try:
        from scrapers.scholar_scraper import ScholarScraper
        from scrapers.arxiv_scraper import ArxivScraper
        
        scholar = ScholarScraper()
        arxiv = ArxivScraper()
        
        print("  ✓ Scholar 爬虫初始化成功")
        print("  ✓ arXiv 爬虫初始化成功")
        print("\n✅ 爬虫模块正常!\n")
        return True
        
    except Exception as e:
        print(f"\n❌ 爬虫测试失败: {e}\n")
        return False


def test_agents():
    """测试 Agents（需要 API Key）"""
    print("🤖 测试 AI Agents...")
    
    import config
    
    if not config.OPENAI_API_KEY:
        print("  ⚠️ 跳过（需要 API Key）\n")
        return True
    
    try:
        from agents.data_collector import DataCollectorAgent
        from agents.research_analyzer import ResearchAnalyzerAgent
        from agents.mentor_agent import MentorAgent
        
        collector = DataCollectorAgent()
        analyzer = ResearchAnalyzerAgent()
        mentor = MentorAgent()
        
        print("  ✓ 数据收集代理初始化成功")
        print("  ✓ 研究分析代理初始化成功")
        print("  ✓ 本科生导师代理初始化成功")
        print("\n✅ Agents 模块正常!\n")
        return True
        
    except Exception as e:
        print(f"\n❌ Agents 测试失败: {e}\n")
        return False


def main():
    """运行所有测试"""
    print("="*60)
    print("🧪 学术开盒 - 模块测试")
    print("="*60)
    print()
    
    results = []
    
    # 运行测试
    results.append(("导入测试", test_imports()))
    results.append(("配置测试", test_config()))
    results.append(("爬虫测试", test_scrapers()))
    results.append(("Agents测试", test_agents()))
    
    # 总结
    print("="*60)
    print("📊 测试总结")
    print("="*60)
    
    for name, passed in results:
        status = "✅ 通过" if passed else "❌ 失败"
        print(f"  {name}: {status}")
    
    all_passed = all(r[1] for r in results)
    
    print()
    if all_passed:
        print("🎉 所有测试通过! 系统可以正常使用。")
        print()
        print("下一步:")
        print("  • Web 界面: streamlit run app.py")
        print("  • 命令行: python main.py \"Professor Name\"")
    else:
        print("⚠️ 部分测试失败，请检查配置和依赖。")
        print()
        print("故障排除:")
        print("  1. 确保运行了: pip install -r requirements.txt")
        print("  2. 确保配置了 .env 文件中的 OPENAI_API_KEY")
        print("  3. 检查网络连接")
    
    print()


if __name__ == "__main__":
    main()
