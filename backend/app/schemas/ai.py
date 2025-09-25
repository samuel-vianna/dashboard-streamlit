from typing import Optional, List, Literal
from datetime import datetime
from sqlmodel import SQLModel
from pydantic import BaseModel, Field

# AI Output
class AIFeedbackOutput(BaseModel):
    score: int
    comment: Optional[str] = None
    timestamp: Optional[datetime] = None
    
class AIFeedbackOutputResponse(BaseModel):
    type: Literal["nps", 'csat']
    feedbacks: List[AIFeedbackOutput]
    
# API Schemas

class FeedbackCreateInput(SQLModel):
    type: Literal["nps", 'csat']
    amount: int = Field(gt=0, le=100, description="Número de avaliações a serem geradas (máximo 100).")
    context: Optional[str] = Field(default=None, description="Contexto para gerar avaliações mais realistas.")
    timestamp: Optional[datetime] = None

class FeedbackCreateResponse(SQLModel):
    total: int
    message: str
    items: List

class FeedbackAnalyze(SQLModel):
    type: str

class CategorizedFeedback(SQLModel):
    type: str
