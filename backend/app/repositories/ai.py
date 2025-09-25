from app.schemas.ai import FeedbackCreateInput, AIFeedbackOutputResponse
from app.services.llm import LLMService
from fastapi import HTTPException

class AiRepository():
    def __init__(self):
        self.service = LLMService()
        
    def generate(self, data: FeedbackCreateInput) -> AIFeedbackOutputResponse:
        try: 
            system_prompt = (
                "Gere {amount} avaliações de clientes no formato {type}.\n"
                "- Se for NPS: notas de 0 a 10.\n"
                "- Se for CSAT: notas de 1 a 5.\n"
                "Cada avaliação deve ter uma nota e um comentário coerente.\n"
                "Se houver contexto, use-o para inspirar os comentários.\n"
                "Se não houver, invente comentários plausíveis."
            )
            
            user_prompt = ("user", "Contexto: {context}")
            
            prompt = [
                ("system", system_prompt),
                user_prompt
            ]
            
            input = {
                "type": data.type,
                "amount": data.amount,
                "context": data.context or "Sem contexto",
                }

            return self.service.request(prompt, AIFeedbackOutputResponse, input)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail=f"Erro ao executar IA: {e}")
        

    def analyze(self):
        try: 
            # prompt = [
            # ('system', 'Você é um assistente de uma empresa de marketing digital.'),
            # ('user', '{input}'),
            #  ]
            # class AnalysisResult(BaseModel):
            #     resposta: str = Field(description="Resposta")
            #     materia: str = Field(description="materia escolar usada na pergunta")

            # input = {"input": "qual os gases nobres?"}
            
            # return self.service.request(prompt, AnalysisResult, input)
            return 'To do...'
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail=f"Erro ao executar IA: {e}")
      

    def categorize(self):
        print('To do...')
        return 
    