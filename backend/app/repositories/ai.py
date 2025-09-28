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
                "se houver branch_id, gere comentários utilizando essa branch_id.\n"
                "Se houver data de envio, gere comentários com datas aleatórias de no máximo {max_time_diff} horas de diferença.\n"
                "Se houver data de envio, os comentários devem ser gerados com datas anteriores a essa data.\n"
                "Os comentários gerados deve possuir origens variadas.\n"
                "Se não houver, invente comentários plausíveis."
            )
            
            user_prompt = ("user", "Contexto: {context}, data de envio: {date}, branch_id: {branch_id}")
            
            prompt = [
                ("system", system_prompt),
                user_prompt
            ]
            
            input = {
                "type": data.type,
                "amount": data.amount,
                "context": data.context or "Sem contexto",
                "date": data.date or "Sem data de envio",
                "max_time_diff": data.max_time_diff or "Sem data de envio",
                "branch_id": data.branch_id or "Sem branch_id",
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
    