"""
主工作流：协调所有 Agent 完成研究任务
"""
from typing import Dict, Any
from langgraph.graph import StateGraph, END

from agents import AgentState
from agents.data_collector import DataCollectorAgent
from agents.research_analyzer import ResearchAnalyzerAgent
from agents.mentor_agent import MentorAgent
from report_generator import ReportGenerator


class ResearchWorkflow:
    """研究工作流"""
    
    def __init__(self):
        self.data_collector = DataCollectorAgent()
        self.research_analyzer = ResearchAnalyzerAgent()
        self.mentor = MentorAgent()
        self.report_generator = ReportGenerator()
        
        # 构建工作流图
        self.workflow = self._build_workflow()
    
    def _build_workflow(self) -> StateGraph:
        """构建 LangGraph 工作流"""
        workflow = StateGraph(AgentState)
        
        # 添加节点
        workflow.add_node("collect_data", self.data_collector.collect_data)
        workflow.add_node("analyze_research", self.research_analyzer.analyze_research)
        workflow.add_node("suggest_tasks", self.mentor.suggest_tasks)
        workflow.add_node("generate_report", self._generate_report_node)
        
        # 定义流程
        workflow.set_entry_point("collect_data")
        workflow.add_edge("collect_data", "analyze_research")
        workflow.add_edge("analyze_research", "suggest_tasks")
        workflow.add_edge("suggest_tasks", "generate_report")
        workflow.add_edge("generate_report", END)
        
        return workflow.compile()
    
    def _generate_report_node(self, state: AgentState) -> AgentState:
        """生成报告节点"""
        print(f"\n{'='*60}")
        print(f"📝 生成最终报告...")
        print(f"{'='*60}\n")
        
        report = self.report_generator.generate_report(
            profile=state["profile"],
            papers=state["papers"],
            research_directions=state.get("research_directions", []),
            key_contributions=state.get("key_contributions", ""),
            field_problems=state.get("field_problems", ""),
            beginner_tasks=state.get("beginner_tasks", [])
        )
        
        state["final_report"] = report
        state["messages"].append("报告生成代理: 最终报告已生成")
        
        return state
    
    def run(self, professor_name: str) -> Dict[str, Any]:
        """
        运行完整的研究工作流
        
        Args:
            professor_name: 教授姓名
            
        Returns:
            包含报告和元数据的字典
        """
        print(f"\n{'='*80}")
        print(f"🎯 开始为 {professor_name} 教授生成学术档案")
        print(f"{'='*80}\n")
        
        # 初始化状态
        initial_state = {
            "professor_name": professor_name,
            "profile": None,
            "papers": [],
            "research_directions": [],
            "key_contributions": "",
            "field_problems": "",
            "beginner_tasks": [],
            "final_report": "",
            "iteration": 0,
            "messages": []
        }
        
        # 执行工作流
        final_state = self.workflow.invoke(initial_state)
        
        # 保存报告
        report_path = self.report_generator.save_report(
            final_state["final_report"],
            professor_name
        )
        
        print(f"\n{'='*80}")
        print(f"✨ 工作流完成！")
        print(f"{'='*80}\n")
        
        print("📋 执行摘要:")
        for msg in final_state["messages"]:
            print(f"  • {msg}")
        
        return {
            "report": final_state["final_report"],
            "report_path": str(report_path),
            "profile": final_state["profile"],
            "papers_count": len(final_state["papers"]),
            "messages": final_state["messages"]
        }


# 命令行接口
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("用法: python workflow.py <教授姓名>")
        print("示例: python workflow.py \"Zhang Wei\"")
        sys.exit(1)
    
    professor_name = sys.argv[1]
    
    workflow = ResearchWorkflow()
    result = workflow.run(professor_name)
    
    print(f"\n✅ 报告已生成: {result['report_path']}")
    print(f"📊 共分析 {result['papers_count']} 篇论文")
