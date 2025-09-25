from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.database import get_session
from app.schemas.user import UserCreate, UserRead
from app.usecases.user import UserUseCase
from typing import List

router = APIRouter(prefix="/users", tags=["users"])

useCase = UserUseCase()

@router.post("/", response_model=UserRead)
def create(user: UserCreate, session: Session = Depends(get_session)):
    return useCase.create_user(session, user)

@router.get("/", response_model=List[UserRead])
def read(session: Session = Depends(get_session)):
    return useCase.get_users(session)

@router.get("/{id}", response_model=UserRead)
def read_by_id(id: int, session: Session = Depends(get_session)):
    return useCase.get_user_by_id(session, id)

@router.delete("/{id}", response_model=None)
def delete(id: int, session: Session = Depends(get_session)):
    return useCase.delete_user(session, id)