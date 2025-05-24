"""
benchmark_tests/token_efficiency_test.py

This benchmark compares token usage between a direct prompt vs FDL-structured prompt.

Goal: Quantify the efficiency gain of FDL prompting.

Author: NGOI-SIGMA
"""

import tiktoken
from agent_core import FDLAgent

# GPT-4 encoder
enc = tiktoken.encoding_for_model("gpt-4")

def count_tokens(text: str) -> int:
    return len(enc.encode(text))

def run_benchmark():
    query = "How should governments regulate AI in the interest of human rights?"

    agent = FDLAgent()
    fdl_prompt = agent.build_prompt(query)

    print("\n🔎 Token Efficiency Benchmark\n")
    print("Raw Query:\n", query)
    print("FDL Prompt:\n", fdl_prompt)

    tokens_raw = count_tokens(query)
    tokens_fdl = count_tokens(fdl_prompt)

    print(f"\n📊 Raw Query Tokens: {tokens_raw}")
    print(f"📊 FDL Prompt Tokens: {tokens_fdl}")
    print(f"✅ Efficiency: {(1 - tokens_fdl / tokens_raw) * 100:.2f}% fewer tokens" if tokens_fdl < tokens_raw else "⚠️ FDL adds structural overhead")

if __name__ == "__main__":
    run_benchmark()
