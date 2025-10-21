"""
测试 API 支持的 LLM 模型
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
api_base = os.getenv("OPENAI_API_BASE")

print("=" * 70)
print("🧪 Testing LLM Models")
print("=" * 70)

client = OpenAI(api_key=api_key, base_url=api_base)

# 常见的 LLM 模型列表
test_models = [
    "gpt-4",
    "gpt-4-turbo",
    "gpt-3.5-turbo",
    "gpt-4o",
    "gpt-4o-mini",
    "deepseek-r1",
    "deepseek-chat",
]

test_message = "Hello"

print(f"\n🔍 Testing API: {api_base}")
print(f"📝 Test message: '{test_message}'\n")

working_models = []

for model in test_models:
    try:
        print(f"  Testing {model}...", end=" ")
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": test_message}],
            max_tokens=10
        )
        print(f"✅ WORKS! (Response: {response.choices[0].message.content[:30]}...)")
        working_models.append(model)
    except Exception as e:
        error_msg = str(e)
        if "not found" in error_msg.lower() or "does not exist" in error_msg.lower():
            print(f"❌ Not available")
        else:
            print(f"❌ Error: {error_msg[:50]}...")

print("\n" + "=" * 70)
print("📊 Summary")
print("=" * 70)

if working_models:
    print(f"✅ Working models ({len(working_models)}):")
    for model in working_models:
        print(f"   - {model}")
    
    print(f"\n💡 Recommendations:")
    print(f"   For paper analysis tasks:")
    
    # 推荐优先级
    if "gpt-4" in working_models:
        print(f"   🌟 Best:  LLM_MODEL=gpt-4")
        print(f"      (High quality, good for academic analysis)")
    if "gpt-4o" in working_models:
        print(f"   🌟 Good:  LLM_MODEL=gpt-4o")
        print(f"      (Faster, still high quality)")
    if "gpt-3.5-turbo" in working_models:
        print(f"   💰 Fast:  LLM_MODEL=gpt-3.5-turbo")
        print(f"      (Cheaper and faster, good enough for most tasks)")
    if "deepseek-chat" in working_models:
        print(f"   ⚡ Alt:   LLM_MODEL=deepseek-chat")
        print(f"      (Good quality, faster than deepseek-r1)")
    
    if "deepseek-r1" in working_models and len(working_models) > 1:
        print(f"\n   ⚠️  Avoid: deepseek-r1 for this task")
        print(f"      (Too slow, overkill for paper summarization)")
else:
    print("❌ No working LLM models found!")
    print("   Please contact your API provider.")

print("=" * 70)
