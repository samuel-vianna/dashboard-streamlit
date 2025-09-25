from sqlmodel import Session
from fastapi import HTTPException
from app.models.user import User
from app.schemas.user import UserCreate
from app.repository.user import UserRepository

repository = UserRepository()

def create_user(session: Session, user_data: UserCreate) -> User:
    user = User(**user_data.dict())
    return repository.create(session, user)

def get_users(session: Session):
    return repository.get_all(session)

def get_user_by_id(session: Session, user_id: str):
    return repository.get_by_id(session, user_id)

def delete_user(session: Session, id: int):
    repository.delete(session, id)
    return True


