"""
API 配置检查脚本
用于诊断 API 配置问题
"""
import os
from dotenv import load_dotenv

load_dotenv()


def check_api_config():
    """打印并返回当前 API 相关的配置摘要（可供脚本或测试调用）。"""
    api_key = os.getenv("OPENAI_API_KEY", "")
    api_base = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    embedding_model = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    llm_model = os.getenv("LLM_MODEL", "gpt-4")

    lines = []
    lines.append("=" * 70)
    lines.append("🔍 API Configuration Check")
    lines.append("=" * 70)

    lines.append(f"\n📋 Current Configuration:")
    lines.append(f"  API Base: {api_base}")
    lines.append(f"  API Key: {'✓ Set' if api_key else '✗ Not set'} ({len(api_key) if api_key else 0} chars)")
    lines.append(f"  Embedding Model: {embedding_model}")
    lines.append(f"  LLM Model: {llm_model}")

    lines.append(f"\n🔍 API Type Detection:")
    if "azure" in api_base.lower():
        lines.append("  ➜ Detected: Azure OpenAI")
        lines.append("  💡 Suggestion: Use 'text-embedding-ada-002' for Azure")
        lines.append("     Update your .env file:")
        lines.append("     EMBEDDING_MODEL=text-embedding-ada-002")
    elif "api.openai.com" in api_base:
        lines.append("  ➜ Detected: OpenAI Official API")
        lines.append("  ✓ 'text-embedding-3-small' should work")
    else:
        lines.append("  ➜ Detected: Third-party API service")
        lines.append("  💡 Suggestion: Check with your API provider which models are supported")
        lines.append("     Common options:")
        lines.append("     - text-embedding-ada-002")
        lines.append("     - text-embedding-3-small")
        lines.append("     - text-embedding-3-large")

    lines.append("\n" + "=" * 70)
    lines.append("💡 Next Steps:")
    lines.append("=" * 70)
    lines.append("1. Update your .env file with the correct EMBEDDING_MODEL")
    lines.append("2. Restart your program")
    lines.append("3. If still having issues, contact your API provider")
    lines.append("=" * 70)

    text = "\n".join(lines)
    return text


if __name__ == '__main__':
    check_api_config()
