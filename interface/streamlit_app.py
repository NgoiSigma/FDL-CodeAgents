"""
interface/streamlit_app.py

Web UI for FDL-CodeAgents using Streamlit.
Allows role selection, query input, chakra resonance control, and real-time feedback.

Author: NGOI-SIGMA
"""

import streamlit as st
from agent_registry import AgentRegistry
from semantic_bridge import SemanticBridge
from chakra_shell import ChakraShell
from agent_memory import MemoryUnit

# Init subsystems
registry = AgentRegistry()
bridge = SemanticBridge()
shell = ChakraShell()
memory = MemoryUnit()

st.set_page_config(page_title="FDL-CodeAgent", layout="centered")

st.title("🧠 FDL-CodeAgent")
st.caption("Semantically-optimized GPT agent using dialectical reasoning")

query = st.text_input("🔎 Your Question or Prompt", placeholder="E.g. What is the nature of contradiction in evolution?")
role = st.selectbox("🎭 Select Agent Role", list(registry.agents.keys()))
emphasis = st.selectbox("🌀 Chakra Emphasis", list(shell.layers.keys()))

if st.button("Generate Response") and query:
    agent = registry.get(role)
    fdl_struct = bridge.interpret(query)
    response = agent.generate_response(query)
    resonant_output = shell.apply(response, emphasis=emphasis)
    memory.store(query, fdl_struct, resonant_output)

    st.subheader("💬 Agent's Response")
    st.success(resonant_output)

    with st.expander("🧠 Memory Snapshot"):
        for i, entry in enumerate(memory.all()):
            st.markdown(f"**{i+1}.** {entry['query']}")
            st.code(entry["response"])

st.markdown("---")
st.caption("Project by NGOI-SIGMA ∷ FDL ∷ SVET")
