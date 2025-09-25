from typing import Optional
from sqlmodel import Session, select
from app.models.user import User
from app.repositories.base import BaseRepository

class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User, 'User')
        
    def get_by_username(self, session: Session, username: str) -> Optional[User]:
            statement = select(self.model).where(self.model.username == username)
            return session.exec(statement).first()