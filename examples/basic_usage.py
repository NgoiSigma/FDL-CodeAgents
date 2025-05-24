"""
examples/basic_usage.py

This script demonstrates how to use the FDL-CodeAgent
to generate a semantically-rich, dialectical response.

Author: NGOI-SIGMA
"""

from agent_core import FDLAgent

# Step 1: Initialize the agent
agent = FDLAgent()

# Step 2: Define your input query
query = "How can society balance technological innovation with ethical responsibility?"

# Step 3: Generate a dialectical response
response = agent.generate_response(query)

# Step 4: Display the result
print("🧠 FDL Response:\n")
print(response)
