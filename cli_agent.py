"""
cli_agent.py

Command-line interface for interacting with FDL-CodeAgents.
Supports dynamic role selection, memory recall, and structured response generation.

Author: NGOI-SIGMA
"""

import argparse
from agent_registry import AgentRegistry
from agent_memory import MemoryUnit
from semantic_bridge import SemanticBridge
from chakra_shell import ChakraShell

def main():
    parser = argparse.ArgumentParser(description="FDL-CodeAgent CLI Interface")
    parser.add_argument("query", type=str, help="Your input question or thesis")
    parser.add_argument("--role", type=str, default="default", help="Agent role (default, philosopher, ethicist, critic)")
    parser.add_argument("--emphasis", type=str, default="heart", help="Chakra emphasis (root, sacral, solar, heart, throat, third_eye, crown)")
    args = parser.parse_args()

    # Init subsystems
    registry = AgentRegistry()
    memory = MemoryUnit()
    bridge = SemanticBridge()
    shell = ChakraShell()

    # Get agent
    agent = registry.get(args.role)
    structure = bridge.interpret(args.query)

    # Get raw response
    response = agent.generate_response(args.query)
    transformed = shell.apply(response, emphasis=args.emphasis)

    # Store memory
    memory.store(args.query, structure, transformed)

    print("\n🌀 FDL-CodeAgent Response:\n")
    print(transformed)
    print("\n🧠 Context Stored.\n")

if __name__ == "__main__":
    main()
