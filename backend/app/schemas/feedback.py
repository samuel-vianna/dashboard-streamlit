from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel
from app.models.feedback import Origin

class FeedbackCreate(SQLModel):
    score: int
    comment: Optional[str] = None
    branch_id: Optional[int] = None
    timestamp: Optional[datetime] = None
    origin: Optional[Origin] = None

class FeedbackUpdate(SQLModel):
    score: Optional[int] = None
    comment: Optional[str] = None

class FeedbackRead(SQLModel):
    id: int
    score: int
    comment: Optional[str] = None
    timestamp: datetime
    branch_id: Optional[int] = None
    origin: Optional[Origin] = None

class FeedbackReadList(SQLModel):
    total: int
    items: list[FeedbackRead]
    
class Summary(SQLModel):
    total: int
    negative: int
    neutral: int
    positive: int
    score: Optional[float] = None
    
class DetailsSummary(Summary):
    origin: Optional[str] = None
    period: Optional[datetime] = None

class FeedbackSummary(Summary):
    details: list[DetailsSummary]