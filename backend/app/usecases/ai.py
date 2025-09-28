from sqlmodel import Session
from fastapi import HTTPException
from app.schemas.ai import FeedbackCreateInput
from app.repositories.ai import AiRepository
from typing import Dict

from app.repositories.nps import NPSRepository
from app.models.nps import NPSFeedback

from app.repositories.csat import CSATRepository
from app.models.csat import CSATFeedback

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
        items = [FeedbackClass(**item.dict() if hasattr(item, "dict") else item) for item in response]
        saved_items = feedback_repo.create_many(session, items)
        
        
        return {"message": "Feedbacks generated successfully",
                'total': len(saved_items),
                'items': saved_items}

    def analyze_feedback(self, session: Session, data: Dict):
        feedback = self.repository.analyze()
        return {'summary': feedback}

    def categorize_feedback(self, session: Session, data: Dict):
        self.repository.categorize()
        return {"message": "Feedback categorized successfully."}
