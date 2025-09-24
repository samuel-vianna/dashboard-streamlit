from sqlmodel import Session, select
from app.models.user import User
from app.schemas.user import UserCreate

def create_user(session: Session, user_data: UserCreate) -> User:
    user = User(**user_data.dict())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_users(session: Session):
    return session.exec(select(User)).all()
