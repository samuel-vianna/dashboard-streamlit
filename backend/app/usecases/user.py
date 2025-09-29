from sqlmodel import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.repositories.user import UserRepository
from app.utils.security import get_password_hash, verify_password, create_access_token


class UserUseCase:
    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, session: Session, data: UserCreate) -> User:
        payload = data.model_dump()
        payload["password"] = get_password_hash(payload["password"])
        user = User(**payload)
        return self.repository.create(session, user)

    def authenticate_user(self, session: Session, username: str, password: str):
        user = self.repository.get_by_username(session, username)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user
    
    def create_token_for_user(self, user: User) -> str:
        return create_access_token(subject=str(user.id))

    def get_users(self, session: Session):
        return self.repository.get_all(session)

    def get_user_by_id(self, session: Session, user_id: str):
        return self.repository.get_by_id(session, user_id)

    def delete_user(self, session: Session, id: int):
        self.repository.delete(session, id)
        return True


