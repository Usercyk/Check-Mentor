"""
AI Agents 模块：使用 LangGraph 构建多代理协作系统
"""
from typing import TypedDict, List, Annotated
from scrapers import Paper, ProfessorProfile


class AgentState(TypedDict):
    """Agent 之间共享的状态"""
    professor_name: str
    profile: ProfessorProfile
    papers: List[Paper]
    research_directions: List[str]
    key_contributions: str
    field_problems: str
    beginner_tasks: List[str]
    final_report: str
    iteration: int
    messages: Annotated[List[str], "Agent 之间的消息"]
