"""
agent_memory.py

Implements basic in-session memory for an FDL-based agent.
Stores user queries, interpreted structures, and generated responses.

Future-ready for persistent embeddings, vector storage or external memory links.

Author: NGOI-SIGMA
"""

from typing import List, Dict

class MemoryUnit:
    def __init__(self):
        self.entries: List[Dict[str, str]] = []

    def store(self, query: str, structure: Dict[str, str], response: str):
        self.entries.append({
            "query": query,
            "fdl": structure,
            "response": response
        })

    def last(self, n: int = 1) -> List[Dict[str, str]]:
        return self.entries[-n:]

    def all(self) -> List[Dict[str, str]]:
        return self.entries

    def reset(self):
        self.entries = []

# Example usage
if __name__ == "__main__":
    from fdl_compiler import FDLCompiler

    mem = MemoryUnit()
    compiler = FDLCompiler()

    q1 = "How can knowledge be transferred between generations?"
    fdl1 = compiler.compile(q1)
    r1 = "By ritual, story, language, and symbolic systems."

    mem.store(q1, fdl1, r1)

    print("🧠 Memory Snapshot:")
    for item in mem.all():
        print(item)
