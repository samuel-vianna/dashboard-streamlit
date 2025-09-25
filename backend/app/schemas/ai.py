from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel

class FeedbackCreate(SQLModel):
    type: str
    score: int
    comment: Optional[str] = None
    timestamp: Optional[datetime] = None

class FeedbackAnalyze(SQLModel):
    type: str

class CategorizedFeedback(SQLModel):
    type: str
