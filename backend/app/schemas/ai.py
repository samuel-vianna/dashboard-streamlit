from typing import Optional, List, Literal
from datetime import datetime
from sqlmodel import SQLModel
from pydantic import BaseModel, Field
from app.models.feedback import Origin
from app.schemas.feedback import FeedbackSummary

# AI Output
class AIFeedbackOutput(BaseModel):
    score: int
    comment: Optional[str] = None
    timestamp: Optional[datetime] = None
    origin: Origin
    branch_id: Optional[int] = None
    
class AIFeedbackOutputResponse(BaseModel):
    type: Literal["nps", 'csat']
    feedbacks: List[AIFeedbackOutput]
    
class AIAnalyzeOutputResponse(BaseModel):
    summary: str
    
# API Schemas

class AIAnalyzeInput(SQLModel):
    nps_data: FeedbackSummary
    csat_data: FeedbackSummary

class FeedbackCreateInput(SQLModel):
    type: Literal["nps", 'csat']
    amount: int = Field(gt=0, le=100, description="Número de avaliações a serem geradas (máximo 100).")
    context: Optional[str] = Field(default=None, description="Contexto para gerar avaliações mais realistas.")
    date: Optional[datetime] = None
    max_time_diff: Optional[int] = None
    branch_id: Optional[int] = None

class FeedbackCreateResponse(SQLModel):
    total: int
    message: str
    items: List

class FeedbackAnalyze(SQLModel):
    type: str

class CategorizedFeedback(SQLModel):
    type: str
