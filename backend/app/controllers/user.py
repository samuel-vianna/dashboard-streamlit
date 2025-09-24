from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.database import get_session
from app.schemas.user import UserCreate, UserRead
from app.usecases.user import create_user, get_users
from typing import List

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead)
def create(user: UserCreate, session: Session = Depends(get_session)):
    return create_user(session, user)

@router.get("/", response_model=List[UserRead])
def read(session: Session = Depends(get_session)):
    return get_users(session)
