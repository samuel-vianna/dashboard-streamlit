from sqlmodel import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.repositories.user import UserRepository
class UserUseCase:
    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, session: Session, data: UserCreate) -> User:
        user = User(**data.model_dump())
        return self.repository.create(session, user)

    def get_users(self, session: Session):
        return self.repository.get_all(session)

    def get_user_by_id(self, session: Session, user_id: str):
        return self.repository.get_by_id(session, user_id)

    def delete_user(self, session: Session, id: int):
        self.repository.delete(session, id)
        return True


