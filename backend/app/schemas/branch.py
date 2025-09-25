from typing import Optional
from sqlmodel import SQLModel

class BranchCreate(SQLModel):
    name: str

class BranchRead(SQLModel):
    id: int
    name: str

class BranchUpdate(SQLModel):
    name: Optional[str] = None
