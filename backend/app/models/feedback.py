from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field
from enum import Enum


class Origin(str, Enum):
    SITE = "site"
    APP = "app"
    TELEFONE = "telefone"
    EMAIL = "email"
    CHAT = "chat"
    PRESENCIAL = "presencial"


class ScoreCategories:
    negative: list[int]
    neutral: list[int]
    positive: list[int]

class Feedback(SQLModel):
    score: int
    comment: Optional[str] = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    origin: Optional[Origin] = None
    sentiment: Optional[str] = None
    
