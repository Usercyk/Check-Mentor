"""
学术开盒 - 主入口文件
提供简单的命令行接口
"""
import sys
from workflow import ResearchWorkflow


def main():
    """主函数"""
    print("="*80)
    print("🎓 学术开盒 (Check-Mentor)")
    print("为物理学本科生准备的导师研究分析工具")
    print("="*80)
    print()
    
    # 获取教授姓名
    if len(sys.argv) > 1:
        professor_name = sys.argv[1]
    else:
        professor_name = input("请输入导师的英文姓名: ").strip()
    
    if not professor_name:
        print("❌ 错误: 请输入导师姓名")
        return
    
    # 运行工作流
    try:
        workflow = ResearchWorkflow()
        result = workflow.run(professor_name)
        
        print("\n" + "="*80)
        print("✨ 分析完成!")
        print("="*80)
        print(f"\n📄 报告路径: {result['report_path']}")
        print(f"📊 分析论文: {result['papers_count']} 篇")
        print(f"🏢 所属机构: {result['profile'].affiliation or '未知'}")
        print("\n💡 提示: 使用 Web 界面获得更好的体验")
        print("   运行命令: streamlit run app.py")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ 用户取消操作")
    except Exception as e:
        print(f"\n❌ 发生错误: {str(e)}")
        print("\n💡 提示: 请检查:")
        print("   1. .env 文件中的 OPENAI_API_KEY 是否正确")
        print("   2. 网络连接是否正常")
        print("   3. 导师姓名是否正确")


if __name__ == "__main__":
    main()
