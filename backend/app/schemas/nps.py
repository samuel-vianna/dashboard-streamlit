from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel

class NPSCreate(SQLModel):
    score: int 
    comment: Optional[str] = None
    branch_id: Optional[int] = None
    timestamp: Optional[datetime] = None

class NPSUpdate(SQLModel):
    score: Optional[int] = None
    comment: Optional[str] = None

class NPSRead(SQLModel):
    id: int
    score: int
    comment: Optional[str] = None
    timestamp: datetime
    branch_id: Optional[int] = None

class NPSReadList(SQLModel):
    total: int
    items: list[NPSRead]