from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel

class CSATCreate(SQLModel):
    score: int
    comment: Optional[str] = None
    branch_id: Optional[int] = None
    timestamp: Optional[datetime] = None

class CSATUpdate(SQLModel):
    score: Optional[int] = None
    comment: Optional[str] = None

class CSATRead(SQLModel):
    id: int
    score: int
    comment: Optional[str] = None
    timestamp: datetime
    branch_id: Optional[int] = None
