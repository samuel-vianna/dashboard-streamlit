from typing import Optional
from sqlmodel import Session, select
from app.models.branch import Branch
from app.repositories.base import BaseRepository

class BranchRepository(BaseRepository[Branch]):
    def __init__(self):
        super().__init__(Branch, 'Branch')
        
    def get_by_name(self, session: Session, name: str) -> Optional[Branch]:
        statement = select(self.model).where(self.model.name == name)
        return session.exec(statement).first()