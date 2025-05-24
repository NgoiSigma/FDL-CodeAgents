"""
agent_core.py

Constructs a resonance-based, meaning-rich response from an FDL-structured query.
Integrates the FDL logic into a prompt for LLM execution.

Author: NGOI-SIGMA
"""

import openai
from fdl_compiler import FDLCompiler
from typing import Dict

class FDLAgent:
    def __init__(self, model: str = "gpt-4", temperature: float = 0.7):
        self.compiler = FDLCompiler()
        self.model = model
        self.temperature = temperature

    def build_prompt(self, query: str) -> str:
        """
        Compile the query into FDL structure and create a prompt.

        Args:
            query (str): User's natural language input.

        Returns:
            str: Optimized prompt for GPT.
        """
        structure = self.compiler.compile(query)
        return self.compiler.to_prompt(structure)

    def generate_response(self, query: str) -> str:
        """
        Calls OpenAI API to generate a response based on the FDL prompt.

        Args:
            query (str): Original user input.

        Returns:
            str: GPT-generated response.
        """
        prompt = self.build_prompt(query)

        # Call to OpenAI (requires key set in environment)
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an FDL-driven reasoning agent. Answer using structured logic."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=600
        )
        return response.choices[0].message["content"]

# Example usage
if __name__ == "__main__":
    agent = FDLAgent()
    query = "What are the ethical risks of deploying autonomous AI in warfare?"
    response = agent.generate_response(query)
    print(response)
