import os
from langchain_core.prompts import ChatPromptTemplate
from .llm_client import LLMClient

class LLMService:
    def __init__(self):
        self.model = os.getenv("AI_MODEL", "gemini")
        self.llm_client = LLMClient(self.model)

    def request(self, prompt: list[tuple[str, str]], schema: type, input: dict) -> str:
        """
        Executa uma chamada para o LLM com base em um prompt, um schema Pydantic e dados de entrada.
        """
    
        llm = self.llm_client.client
        
        formatted_prompt = ChatPromptTemplate.from_messages(prompt)
        structured_llm = llm.with_structured_output(schema)
        
        chain = formatted_prompt | structured_llm
        return chain.invoke(input)
        
        