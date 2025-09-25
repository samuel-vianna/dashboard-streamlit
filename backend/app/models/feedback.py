from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class Feedback(SQLModel):
    score: int
    comment: Optional[str] = None
    # use factory for UTC timestamp
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))