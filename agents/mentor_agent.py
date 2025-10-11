"""
本科生导师代理：为本科生设计合适的科研入门任务
"""
from typing import List
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from agents import AgentState
import config


class MentorAgent:
    """本科生导师代理"""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model=config.LLM_MODEL,
            temperature=0.5,  # 稍高的温度以增加创造性
            api_key=config.OPENAI_API_KEY,
            base_url=config.OPENAI_API_BASE
        )
    
    def suggest_tasks(self, state: AgentState) -> AgentState:
        """
        为本科生设计科研入门任务
        
        Args:
            state: 当前状态
            
        Returns:
            更新后的状态
        """
        print(f"\n{'='*60}")
        print(f"🎓 本科生导师代理开始工作...")
        print(f"{'='*60}\n")
        
        research_directions = state.get("research_directions", [])
        field_problems = state.get("field_problems", "")
        
        if not research_directions:
            print("⚠️ 缺少研究方向信息，跳过任务设计")
            return state
        
        print("💡 设计本科生科研任务...")
        tasks = self._design_tasks(research_directions, field_problems)
        
        # 更新状态
        state["beginner_tasks"] = tasks
        state["messages"].append(
            f"本科生导师代理: 设计了 {len(tasks)} 个科研任务"
        )
        
        return state
    
    def _design_tasks(
        self, 
        research_directions: List[str], 
        field_problems: str
    ) -> List[str]:
        """设计科研任务"""
        prompt = f"""
你是一位经验丰富的物理学本科生科研导师。基于以下研究方向和领域问题，为有意向加入该课题组的本科生设计3-5个**循序渐进**的科研入门任务。

研究方向:
{chr(10).join([f"{i+1}. {d}" for i, d in enumerate(research_directions)])}

领域核心问题:
{field_problems}

要求:
1. **任务难度递增**: 从简单到复杂，适合本科生的知识水平
2. **具体可执行**: 每个任务都要有明确的目标和可操作的步骤
3. **覆盖多种技能**: 包括文献调研、编程、数据分析、理论推导等
4. **时间合理**: 每个任务预计1-4周完成

任务类型示例:
- **文献综述**: 针对某个具体子方向的文献调研和总结
- **经典复现**: 用Python/Matlab复现某篇重要论文的部分结果
- **数据分析**: 学习处理和可视化实验/模拟数据
- **理论推导**: 理解并推导某个关键理论公式
- **软件学习**: 掌握领域常用的科研工具（如VASP, COMSOL等）

格式要求:
每个任务包含: 
- 任务名称
- 具体描述（100-150字）
- 预期成果
- 预计时间

请直接给出任务列表:
"""
        
        messages = [
            SystemMessage(content="你是一位经验丰富的物理学本科生科研导师。"),
            HumanMessage(content=prompt)
        ]
        
        response = self.llm.invoke(messages)
        
        # 解析任务（简单按段落分割）
        tasks_text = response.content
        tasks = []
        
        current_task = []
        for line in tasks_text.split('\n'):
            line = line.strip()
            if line.startswith('###') or line.startswith('**任务'):
                if current_task:
                    tasks.append('\n'.join(current_task))
                current_task = [line]
            elif line:
                current_task.append(line)
        
        if current_task:
            tasks.append('\n'.join(current_task))
        
        # 如果解析失败，返回原始文本
        if not tasks:
            tasks = [tasks_text]
        
        print(f"  ✓ 设计了 {len(tasks)} 个科研任务")
        for i, task in enumerate(tasks, 1):
            preview = task.split('\n')[0][:60]
            print(f"    {i}. {preview}...")
        
        return tasks
