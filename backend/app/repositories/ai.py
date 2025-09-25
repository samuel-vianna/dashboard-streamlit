from typing import TypeVar, Generic, Type, List, Optional, Dict, Any, Text
from app.schemas.ai import FeedbackCreate
from sqlmodel import SQLModel, Session, select

class AiRepository():
    def __init__(self):
        self.model = None
        
    def generate(self, data: FeedbackCreate) -> list:
        return [{"type": "NPS", "score": 8, "comment": "good"}, {"type": "CSAT", "score": 7, "comment": "ok"}]

    def analyze(self):
        feedback = 'The feedback is analyzed successfully.'
        return feedback

    def categorize(self):
        print('To do...')
        return 
    