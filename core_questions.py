"""
核心问题定义
用于评估论文与教授研究方向的相关性
"""

CORE_QUESTIONS = {
    "research_domain": {
        "question": "What is the main research domain and field of this paper? Does it align with the professor's research interests?",
        "question_zh": "这篇论文的主要研究领域是什么？是否与教授的研究兴趣相符？",
        "weight": 0.3
    },
    
    "technical_approach": {
        "question": "What technical methods and approaches are used in this paper? Are they commonly used in the professor's lab?",
        "question_zh": "这篇论文使用了什么技术方法和途径？这些方法是否在教授的实验室中常用？",
        "weight": 0.25
    },
    
    "novelty": {
        "question": "What is the novelty and innovation of this paper? Does it introduce new concepts or methods?",
        "question_zh": "这篇论文的新颖性和创新点是什么？是否引入了新概念或新方法？",
        "weight": 0.2
    },
    
    "beginner_friendly": {
        "question": "Is this paper suitable for undergraduate students to learn and reproduce? Does it provide accessible entry points?",
        "question_zh": "这篇论文是否适合本科生学习和复现？是否提供了易于入门的切入点？",
        "weight": 0.15
    },
    
    "practical_value": {
        "question": "What is the practical application value of this paper? Can it be applied to real-world problems?",
        "question_zh": "这篇论文的实际应用价值是什么？能否应用于实际问题？",
        "weight": 0.1
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
