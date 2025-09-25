from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.database import get_session
from app.schemas.csat import CSATCreate, CSATRead, CSATUpdate
from app.usecases.csat import (
    create_csat,
    get_csats,
    update_csat,
    delete_csat,
)
from typing import List

router = APIRouter(prefix="/csat", tags=["csat"])

@router.post("/", response_model=CSATRead)
def create(item: CSATCreate, session: Session = Depends(get_session)):
    return create_csat(session, item)

@router.get("/", response_model=List[CSATRead])
def read(session: Session = Depends(get_session)):
    return get_csats(session)

@router.put("/{id}", response_model=CSATRead)
def update(branch: CSATUpdate, id: int, session: Session = Depends(get_session)):
    return update_csat(session, id, branch)

@router.delete("/{id}", response_model=None)
def delete(id: int, session: Session = Depends(get_session)):
   return delete_csat(session, id)