from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.services.database import get_session
from app.schemas.nps import NPSCreate, NPSRead, NPSReadList, NPSUpdate
from app.usecases.nps import NPSUseCase
from typing import List

router = APIRouter(prefix="/nps", tags=["nps"])

useCase = NPSUseCase()

@router.post("/", response_model=NPSRead)
def create(item: NPSCreate, session: Session = Depends(get_session)):
    return useCase.create_nps(session, item)

@router.get("/", response_model=NPSReadList)
def read(session: Session = Depends(get_session)):
    return useCase.get_nps(session)

@router.put("/{id}", response_model=NPSRead)
def update(branch: NPSUpdate, id: int, session: Session = Depends(get_session)):
    return useCase.update_nps(session, id, branch)

@router.delete("/{id}", response_model=None)
def delete(id: int, session: Session = Depends(get_session)):
   return useCase.delete_nps(session, id)