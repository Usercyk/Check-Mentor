"""
测试 API 支持的 embedding 模型
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
api_base = os.getenv("OPENAI_API_BASE")

print("=" * 70)
print("🧪 Testing Embedding Models")
print("=" * 70)

client = OpenAI(api_key=api_key, base_url=api_base)

# 常见的 embedding 模型列表
test_models = [
    "text-embedding-ada-002",
    "text-embedding-3-small",
    "text-embedding-3-large",
    "embedding-ada-002",
    "text-embedding-v1",
]

test_text = "Hello, this is a test."

print(f"\n🔍 Testing API: {api_base}")
print(f"📝 Test text: '{test_text}'\n")

working_models = []

for model in test_models:
    try:
        print(f"  Testing {model}...", end=" ")
        response = client.embeddings.create(
            input=test_text,
            model=model
        )
        print(f"✅ WORKS! (dimension: {len(response.data[0].embedding)})")
        working_models.append(model)
    except Exception as e:
        error_msg = str(e)
        if "does not work" in error_msg or "not found" in error_msg or "OperationNotSupported" in error_msg:
            print(f"❌ Not supported")
        else:
            print(f"❌ Error: {error_msg[:50]}...")

print("\n" + "=" * 70)
if working_models:
    print(f"✅ Working models: {', '.join(working_models)}")
    print(f"\n💡 Update your .env file:")
    print(f"   EMBEDDING_MODEL={working_models[0]}")
else:
    print("❌ No working embedding models found!")
    print("   Please contact your API provider for supported models.")
print("=" * 70)
