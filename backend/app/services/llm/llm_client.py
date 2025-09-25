import os

class LLMClient():
    def __init__(self, model: str = "gemini"):
        self.model = model

    @property
    def client(self):
        match self.model:
            case 'gemini':
                from langchain_google_genai import ChatGoogleGenerativeAI

                if "GOOGLE_API_KEY" not in os.environ:
                    raise Exception("GOOGLE_API_KEY não encontrado")
                    
                return ChatGoogleGenerativeAI(model="gemini-2.5-flash")
            case _:
                raise Exception(f"Modelo '{self.model}' não suportado")
            