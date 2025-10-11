"""
Streamlit Web 应用：为"学术开盒"项目提供友好的用户界面
"""
import streamlit as st
from pathlib import Path
import traceback

from workflow import ResearchWorkflow
import config


# 页面配置
st.set_page_config(
    page_title="学术开盒 - 导师研究分析",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义样式
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .warning-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        color: #856404;
    }
</style>
""", unsafe_allow_html=True)


def main():
    """主应用"""
    
    # 标题
    st.markdown('<div class="main-header">🎓 学术开盒</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-header">为物理学本科生准备的导师研究分析工具</div>', 
        unsafe_allow_html=True
    )
    
    # 侧边栏
    with st.sidebar:
        st.header("📋 关于本项目")
        st.markdown("""
        **学术开盒**旨在帮助物理学本科生：
        
        1. 🔍 了解导师的研究方向
        2. 🏆 发现导师的代表性贡献
        3. 🎯 理解领域的核心问题
        4. 🚀 获得科研入门建议
        
        ---
        
        **使用方法**：
        - 输入导师的英文姓名
        - 点击"开始分析"
        - 等待 AI 生成报告
        
        ---
        
        **数据来源**：
        - Google Scholar
        - arXiv
        - 导师个人主页
        """)
        
        st.header("⚙️ 配置")
        
        # 检查配置
        api_key_status = "✅ 已配置" if config.OPENAI_API_KEY else "❌ 未配置"
        st.write(f"OpenAI API Key: {api_key_status}")
        st.write(f"模型: {config.LLM_MODEL}")
        
        if not config.OPENAI_API_KEY:
            st.warning("⚠️ 请在 .env 文件中配置 OPENAI_API_KEY")
    
    # 主界面
    st.markdown("---")
    
    # 输入区域
    col1, col2 = st.columns([3, 1])
    
    with col1:
        professor_name = st.text_input(
            "请输入导师的英文姓名",
            placeholder="例如: Zhang Wei",
            help="请使用导师在论文上的常用英文名"
        )
    
    with col2:
        st.write("")  # 占位
        st.write("")  # 占位
        analyze_button = st.button("🚀 开始分析", type="primary", use_container_width=True)
    
    # 高级选项（可折叠）
    with st.expander("⚙️ 高级选项"):
        max_papers = st.slider(
            "每个来源最多获取的论文数",
            min_value=5,
            max_value=20,
            value=config.MAX_PAPERS_PER_SOURCE,
            step=5
        )
        config.MAX_PAPERS_PER_SOURCE = max_papers
        
        recent_years = st.slider(
            "分析最近几年的论文",
            min_value=3,
            max_value=10,
            value=config.RECENT_YEARS,
            step=1
        )
        config.RECENT_YEARS = recent_years
    
    # 执行分析
    if analyze_button:
        if not professor_name:
            st.error("❌ 请输入导师姓名")
            return
        
        if not config.OPENAI_API_KEY:
            st.error("❌ 请先配置 OpenAI API Key（在 .env 文件中）")
            return
        
        # 创建进度显示
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # 初始化工作流
            status_text.text("🔧 初始化工作流...")
            progress_bar.progress(10)
            workflow = ResearchWorkflow()
            
            # 执行分析
            status_text.text(f"🔍 正在分析 {professor_name} 教授...")
            progress_bar.progress(20)
            
            # 创建容器显示实时日志
            log_container = st.container()
            
            with st.spinner("正在收集和分析数据，这可能需要几分钟..."):
                result = workflow.run(professor_name)
            
            progress_bar.progress(100)
            status_text.text("✅ 分析完成！")
            
            # 显示成功消息
            st.success(f"✅ 成功为 {professor_name} 教授生成学术档案！")
            
            # 显示统计信息
            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("📚 分析论文数", result['papers_count'])
            with col2:
                st.metric("🏢 所属机构", result['profile'].affiliation or "未知")
            with col3:
                st.metric("🔗 个人主页", "有" if result['profile'].homepage else "无")
            
            # 显示报告
            st.markdown("---")
            st.markdown("## 📄 生成的报告")
            
            # 在两列中显示：一列是报告预览，一列是下载按钮
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.markdown(result['report'])
            
            with col2:
                st.download_button(
                    label="📥 下载报告",
                    data=result['report'],
                    file_name=f"{professor_name.replace(' ', '_')}_report.md",
                    mime="text/markdown"
                )
                
                st.info(f"💾 报告已保存至:\n{result['report_path']}")
            
            # 显示执行日志
            with st.expander("📋 查看执行日志"):
                for msg in result['messages']:
                    st.text(msg)
        
        except Exception as e:
            progress_bar.progress(0)
            status_text.text("")
            st.error(f"❌ 发生错误: {str(e)}")
            
            with st.expander("🔍 查看详细错误信息"):
                st.code(traceback.format_exc())
    
    # 底部信息
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #888; font-size: 0.9rem;'>
        <p>💡 提示：本报告由 AI 自动生成，建议结合导师个人主页和代表性论文进行深入了解。</p>
        <p>📧 问题反馈 | 🌟 项目地址 | 📖 使用文档</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
