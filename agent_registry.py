"""
agent_registry.py

Central registry of FDL agent roles.
Allows modular selection of different agent personas or processing styles.

Author: NGOI-SIGMA
"""

from agent_core import FDLAgent
from typing import Dict, Callable


class AgentRegistry:
    def __init__(self):
        self.agents: Dict[str, Callable[..., FDLAgent]] = {}

        self.register("default", lambda: FDLAgent())
        self.register("ethicist", lambda: FDLAgent(model="gpt-4", temperature=0.3))
        self.register("philosopher", lambda: FDLAgent(model="gpt-4", temperature=0.6))
        self.register("critic", lambda: FDLAgent(model="gpt-4", temperature=0.8))

    def register(self, name: str, constructor: Callable[..., FDLAgent]):
        self.agents[name] = constructor

    def get(self, name: str) -> FDLAgent:
        return self.agents.get(name, self.agents["default"])()


# Example usage
if __name__ == "__main__":
    registry = AgentRegistry()

    for role in registry.agents:
        print(f"🧠 Loaded agent: {role}")

    agent = registry.get("philosopher")
    response = agent.generate_response("What is the role of contradiction in social evolution?")
    print(response)
