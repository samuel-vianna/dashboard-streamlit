from sqlmodel import Session
from app.schemas.ai import FeedbackCreate
from app.repositories.nps import NPSRepository
from app.repositories.csat import CSATRepository
from app.repositories.ai import AiRepository
from typing import Dict

class AIUseCase:
    def __init__(self):
        self.repository = AiRepository()
        self.nps_repository = NPSRepository()
        self.csat_repository = CSATRepository()

    def generate_feedback(self, session: Session, data: FeedbackCreate):
        print(data)
        response = self.repository.generate(data)
        
        return {"message": "Feedback generated successfully", 'generated': len(response)}

    def analyze_feedback(self, session: Session, data: Dict):
        feedback = self.repository.analyze()
        return {'summary': feedback}

    def categorize_feedback(self, session: Session, data: Dict):
        self.repository.categorize()
        return {"message": "Feedback categorized successfully."}
