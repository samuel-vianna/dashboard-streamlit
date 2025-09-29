from app.schemas.ai import FeedbackCreateInput, AIFeedbackOutputResponse, AIAnalyzeInput, AIAnalyzeOutputResponse, AICategorizeOutputResponse
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
                "A resposta deve possuir no máximo de 300 caracteres."
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
        

    def analyze(self, data: AIAnalyzeInput):
        try: 
            system_prompt = (
                "Você é um assistente especializado em análise de feedback.\n"
                "Sua tarefa é analisar os dados fornecidos de NPS e CSAT e gerar um texto resumido que contenha:\n"
                "  - Um resumo geral sobre as notas e desempenho.\n"
                "  - O que acha dos resultados.\n"
                "  - Pontos de atenção (o que pode melhorar).\n"
                "  - Aspectos positivos identificados.\n"
                "  - Aspectos negativos identificados.\n\n"
                " - Analise os dados em 'details' para gerar insights específicos por origem e período.\n"
            )

            
            user_prompt = ("user", "nps: {nps}, csat: {csat}")
            
            prompt = [
                ("system", system_prompt),
                user_prompt
            ]
            
            input = {"nps": data.nps_data, "csat": data.csat_data}

            return self.service.request(prompt, AIAnalyzeOutputResponse, input)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail=f"Erro ao executar IA: {e}")
        

    def categorize(self, comments: list[str]):
        try: 
            sentiments = [
                "feliz", "grato", "confuso", "frustrado", "impaciente",
                "triste", "agradecido", "surpreso", "estressado", "indiferente"
                ]

            
            system_prompt = (
                "Você é um assistente especializado em análise de feedback.\n"
                "Sua tarefa é analisar os comentários fornecidos de NPS e CSAT e categorizar os comentários.\n"
                " - Analise os comentários e o classifique de acordo com sentimento.\n"
                " - Lista de possíveis sentimentos: {sentiments}\n"
                " - A lista deve possuir relação de 1 para 1. Ou seja, a mesma quantidade de comentários fornecidos deve ser a quantidade de sentimentos, retornados na mesma ordem.\n"
            )
            
            user_prompt = ("user", "comentarios: {comments}")
            
            prompt = [
                ("system", system_prompt),
                user_prompt
            ]
            
            input = {
                "comments": comments,
                "sentiments": sentiments
                }

            return self.service.request(prompt, AICategorizeOutputResponse, input)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail=f"Erro ao executar IA: {e}")
    