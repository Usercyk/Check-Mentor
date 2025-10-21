"""
核心问题定义
用于评估论文与教授研究方向的相关性
"""

CORE_QUESTIONS = {
    "professor_interests": {
        "question": "What research directions is the professor interested in, and what contributions has he made to these areas?",
        "question_zh": "老师对哪些方向感兴趣，他对此有哪些贡献？",
        "weight": 0.4
    },
    
    "field_problems": {
        "question": "What problems are scholars in these research directions concerned about—what are the main problems within these directions?",
        "question_zh": "这些方向的学者们都在关心什么问题——这些方向内的主要问题是什么？",
        "weight": 0.35
    },
    
    "undergraduate_projects": {
        "question": "What projects in these research directions can undergraduate students participate in?",
        "question_zh": "这些方向有哪些本科生可以参与的项目？",
        "weight": 0.25
    }
}


def get_question(key: str, language: str = "en") -> str:
    """
    获取指定问题的文本
    
    Args:
        key: 问题的键值
        language: 语言 ('en' 或 'zh')
    
    Returns:
        问题文本
    """
    if key not in CORE_QUESTIONS:
        raise ValueError(f"Unknown question key: {key}")
    
    question_key = "question" if language == "en" else "question_zh"
    return CORE_QUESTIONS[key][question_key]


def get_all_questions(language: str = "en") -> dict:
    """
    获取所有问题
    
    Args:
        language: 语言 ('en' 或 'zh')
    
    Returns:
        问题字典
    """
    question_key = "question" if language == "en" else "question_zh"
    return {key: value[question_key] for key, value in CORE_QUESTIONS.items()}


def get_question_weight(key: str) -> float:
    """
    获取问题的权重
    
    Args:
        key: 问题的键值
    
    Returns:
        权重值
    """
    if key not in CORE_QUESTIONS:
        raise ValueError(f"Unknown question key: {key}")
    
    return CORE_QUESTIONS[key]["weight"]
