"""
API 配置检查脚本
用于诊断 API 配置问题
"""
import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 70)
print("🔍 API Configuration Check")
print("=" * 70)

api_key = os.getenv("OPENAI_API_KEY", "")
api_base = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
embedding_model = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
llm_model = os.getenv("LLM_MODEL", "gpt-4")

print(f"\n📋 Current Configuration:")
print(f"  API Base: {api_base}")
print(f"  API Key: {'✓ Set' if api_key else '✗ Not set'} ({len(api_key) if api_key else 0} chars)")
print(f"  Embedding Model: {embedding_model}")
print(f"  LLM Model: {llm_model}")

print(f"\n🔍 API Type Detection:")
if "azure" in api_base.lower():
    print("  ➜ Detected: Azure OpenAI")
    print("  💡 Suggestion: Use 'text-embedding-ada-002' for Azure")
    print("     Update your .env file:")
    print("     EMBEDDING_MODEL=text-embedding-ada-002")
elif "api.openai.com" in api_base:
    print("  ➜ Detected: OpenAI Official API")
    print("  ✓ 'text-embedding-3-small' should work")
else:
    print("  ➜ Detected: Third-party API service")
    print("  💡 Suggestion: Check with your API provider which models are supported")
    print("     Common options:")
    print("     - text-embedding-ada-002")
    print("     - text-embedding-3-small")
    print("     - text-embedding-3-large")

print("\n" + "=" * 70)
print("💡 Next Steps:")
print("=" * 70)
print("1. Update your .env file with the correct EMBEDDING_MODEL")
print("2. Restart your program")
print("3. If still having issues, contact your API provider")
print("=" * 70)
