"""
全面模型可用性检测脚本
- 读取 .env 中的 OPENAI_API_KEY 和 OPENAI_API_BASE
- 对用户提供的模型列表分别测试：chat（LLM）和 embeddings（embedding 模型）
- 把测试结果以 JSON 写入 output/models_test_results.json

注意：脚本会按顺序测试模型，遇到 API 错误会记录并继续。
"""
import os
import time
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
api_base = os.getenv("OPENAI_API_BASE")

client = OpenAI(api_key=api_key, base_url=api_base)

# 用户提供的混合列表（来自您的清单）
models = [
    "deepseek-r1",
    "deepseek-r1-0528",
    "deepseek-v3",
    "deepseek-v3.1",
    "qwen-coder-plus",
    "qwen-coder-plus-latest",
    "qwen-coder-turbo",
    "qwen-coder-turbo-latest",
    "qwen-long",
    "qwen-math-plus",
    "qwen-math-plus-latest",
    "qwen-math-turbo",
    "qwen-math-turbo-latest",
    "qwen-max-latest",
    "qwen-plus-2025-07-14",
    "qwen-plus-2025-09-11",
    "qwen-turbo",
    "qwen-turbo-latest",
    "qwen2.5-14b-instruct",
    "qwen2.5-32b-instruct",
    "qwen2.5-3b-instruct",
    "qwen2.5-72b-instruct",
    "qwen2.5-coder-0.5b-instruct",
    "qwen2.5-coder-14b-instruct",
    "qwen2.5-coder-32b-instruct",
    "qwen2.5-coder-3b-instruct",
    "qwen2.5-coder-7b-instruct",
    "qwen2.5-math-72b-instruct",
    "qwen2.5-math-7b-instruct",
    "qwen3-1.7b",
    "qwen3-14b",
    "qwen3-235b-a22b",
    "qwen3-235b-a22b-instruct",
    "qwen3-235b-a22b-thinking",
    "qwen3-30b-a3b",
    "qwen3-coder-480b-a35b-instruct",
    "qwen3-coder-flash",
    "qwen3-coder-flash-2025-07-28",
    "qwen3-coder-plus",
    "qwen3-coder-plus-2025-07-22",
    "qwen3-max-preview",
    "qwen3-next-80b-a3b-instruct",
    "qwen3-next-80b-a3b-thinking",
    "qwen3-vl-plus",
    "qwq-32b",
    "claude-3-7-sonnet-20250219",
    "claude-haiku-4-5",
    "claude-opus-4-20250514",
    "claude-sonnet-4-20250514",
    "claude-sonnet-4-5-20250929",
    "deepseek-v3-250324",
    "DeepSeek-V3.2-Exp",
    "DeepSeek-V3.2-Exp-Think",
    "gemini-2.5-flash",
    "gemini-2.5-pro",
    "glm-4.6",
    "gpt-4.1",
    "gpt-4.1-mini",
    "gpt-4.1-nano",
    "gpt-4o-2024-11-20",
    "gpt-4o-mini",
    "gpt-5",
    "gpt-5-mini",
    "gpt-5-nano",
    "o1",
    "o3-2025-04-16",
    "o4-mini",
    "text-embedding-v1",
    "text-embedding-v2",
    "text-embedding-v3",
    "text-embedding-v4",
    "claude-3-7-sonnet-20250219",
    "text-embedding-3-large",
    "text-embedding-3-small",
    "text-embedding-ada-002",
]

# Split into embedding candidates and LLM candidates by simple heuristic
embedding_candidates = [m for m in models if "embedding" in m or m.startswith("text-embedding")]
llm_candidates = [m for m in models if m not in embedding_candidates]

results = {
    "api_base": api_base,
    "checked_at": time.strftime("%Y-%m-%d %H:%M:%S"),
    "llm": {},
    "embeddings": {}
}

print("Starting full model availability test...")

# Test LLMs (chat completion)
for name in llm_candidates:
    try:
        print(f"Testing LLM: {name}...", end=" ")
        resp = client.chat.completions.create(
            model=name,
            messages=[{"role":"user","content":"Hello, can you respond briefly?"}],
            max_tokens=8
        )
        # Note: some providers return different response shapes
        ok = True
        snippet = None
        try:
            snippet = resp.choices[0].message.content
        except Exception:
            snippet = str(resp)[:80]
        print("WORKS")
        results["llm"][name] = {"ok": True, "detail": str(snippet)[:200]}
    except Exception as e:
        err = str(e)
        print("FAIL", err.split('\n')[0][:120])
        results["llm"][name] = {"ok": False, "error": err[:1000]}
    time.sleep(0.2)

# Test embedding models
for name in embedding_candidates:
    try:
        print(f"Testing Embedding: {name}...", end=" ")
        r = client.embeddings.create(input=["test"], model=name)
        dim = None
        try:
            dim = len(r.data[0].embedding)
        except Exception:
            dim = None
        print("WORKS", f"dim={dim}")
        results["embeddings"][name] = {"ok": True, "dim": dim}
    except Exception as e:
        err = str(e)
        print("FAIL", err.split('\n')[0][:120])
        results["embeddings"][name] = {"ok": False, "error": err[:1000]}
    time.sleep(0.2)

# Save results
os.makedirs("output", exist_ok=True)
out_path = os.path.join("output", "models_test_results.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nTest complete.")
print("Results written to:", out_path)
