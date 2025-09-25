from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.schemas.csat import CSATCreate, CSATRead, CSATReadList, CSATUpdate
from app.services.database import get_session
from app.usecases.csat import CSATUseCase
from typing import List

router = APIRouter(prefix="/csat", tags=["csat"])

useCase = CSATUseCase()

@router.post("/", response_model=CSATRead)
def create(item: CSATCreate, session: Session = Depends(get_session)):
    return useCase.create_csat(session, item)

@router.get("/", response_model=CSATReadList)
def read(session: Session = Depends(get_session)):
    return useCase.get_csats(session)

@router.put("/{id}", response_model=CSATRead)
def update(branch: CSATUpdate, id: int, session: Session = Depends(get_session)):
    return useCase.update_csat(session, id, branch)

@router.delete("/{id}", response_model=None)
def delete(id: int, session: Session = Depends(get_session)):
   return useCase.delete_csat(session, id)