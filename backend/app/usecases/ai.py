from sqlmodel import Session
from app.schemas.ai import FeedbackCreate

class AIUseCase:
    def __init__(self, repository=None):
        self.repository = repository

    def generate_feedback(self, session: Session, data: FeedbackCreate):
        print(data)
        # self.repository.create(session, branch)
        return {"message": "Feedback generated successfully"}

    def analyze_feedback(self, session: Session, data: list):
        return {"summary": "The feedback is analyzed successfully."}

    def categorize_feedback(self, session: Session, data: list):
        return {"message": "Feedback categorized successfully."}
