"""
api_wrapper.py

Provides a smart interface to OpenAI's API with automatic token monitoring,
request compression, and future routing logic for semantic efficiency.

Author: NGOI-SIGMA
"""

import os
import openai
from typing import List, Dict, Any

class OpenAIWrapper:
    def __init__(self, model: str = "gpt-4", temperature: float = 0.7, max_tokens: int = 800):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.api_key = os.getenv("OPENAI_API_KEY")

        if not self.api_key:
            raise EnvironmentError("OPENAI_API_KEY environment variable is not set.")

        openai.api_key = self.api_key

    def send(self, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        Sends a chat completion request to the OpenAI API.

        Args:
            messages (List[Dict[str, str]]): Chat messages (system/user/assistant)

        Returns:
            Dict[str, Any]: Response JSON
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            return response
        except Exception as e:
            return {"error": str(e)}

    def get_clean_output(self, response: Dict[str, Any]) -> str:
        """
        Extracts and returns the response message.

        Args:
            response (Dict): OpenAI API response

        Returns:
            str: Assistant's reply or error message
        """
        if "error" in response:
            return f"[API Error] {response['error']}"
        try:
            return response["choices"][0]["message"]["content"].strip()
        except (KeyError, IndexError):
            return "[Error parsing API response]"

# Example use
if __name__ == "__main__":
    wrapper = OpenAIWrapper()
    msgs = [
        {"role": "system", "content": "You are a dialectical reasoning assistant."},
        {"role": "user", "content": "What is the difference between freedom and responsibility in social systems?"}
    ]
    raw = wrapper.send(msgs)
    print(wrapper.get_clean_output(raw))
