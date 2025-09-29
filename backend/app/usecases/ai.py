from sqlmodel import Session
from fastapi import HTTPException
from app.schemas.ai import FeedbackCreateInput, AIAnalyzeInput
from app.repositories.ai import AiRepository
from app.repositories.nps import NPSRepository
from app.repositories.csat import CSATRepository
from app.models.csat import CSATFeedback
from app.models.nps import NPSFeedback
from app.utils.categorize_comments import categorize_comments

class AIUseCase:
    def __init__(self):
        self.repository = AiRepository()
        self.nps_repository = NPSRepository()
        self.csat_repository = CSATRepository()

    def generate_feedback(self, session: Session, data: FeedbackCreateInput):
        response = self.repository.generate(data).feedbacks
        
        if len(response) == 0:
            raise HTTPException(status_code=400, detail="No feedback generated.")
        
        if(data.type == 'nps'):
            feedback_repo = self.nps_repository
            FeedbackClass = NPSFeedback         
        elif(data.type == 'csat'):
            feedback_repo = self.csat_repository
            FeedbackClass = CSATFeedback
        else:
            raise HTTPException(status_code=400, detail="Tipo de feedback inválido")
        
        # update data using selected feedback
        items = [FeedbackClass(**item.model_dump() if hasattr(item, "dict") else item) for item in response]
        saved_items = feedback_repo.create_many(session, items)
        
        
        return {"message": "Feedbacks generated successfully",
                'total': len(saved_items),
                'items': saved_items}

    def analyze_feedback(self,data: AIAnalyzeInput):
        feedback = self.repository.analyze(data)
        return feedback

    def categorize_feedback(self, session: Session):
        
        # ------------------------------
        # NPS
        # ------------------------------
        nps_response = categorize_comments(
            session=session,
            repository=self.nps_repository,
            categorize_fn=self.repository.categorize, 
            limit=50,
            field="sentiment"
        )
            
        # ------------------------------
        # CSAT
        # ------------------------------
        csat_response = categorize_comments(
            session=session,
            repository=self.csat_repository,
            categorize_fn=self.repository.categorize,
            limit=50,
            field="sentiment"
            )
        
        return {
            "message": f"{nps_response + csat_response} Comentário(s) categorizados com successo!",
            "nps": nps_response,
            "csat": csat_response
            }
