from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.database import get_session
from app.schemas.nps import NPSCreate, NPSRead, NPSUpdate
from app.usecases.nps import (
    create_nps,
    get_nps,
    update_nps,
    delete_nps,
)
from typing import List

router = APIRouter(prefix="/nps", tags=["nps"])

@router.post("/", response_model=NPSRead)
def create(item: NPSCreate, session: Session = Depends(get_session)):
    return create_nps(session, item)

@router.get("/", response_model=List[NPSRead])
def read(session: Session = Depends(get_session)):
    return get_nps(session)

@router.put("/{id}", response_model=NPSRead)
def update(branch: NPSUpdate, id: int, session: Session = Depends(get_session)):
    return update_nps(session, id, branch)

@router.delete("/{id}", response_model=None)
def delete(id: int, session: Session = Depends(get_session)):
   return delete_nps(session, id)