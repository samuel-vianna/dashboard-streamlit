from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from typing import Optional
from app.models.feedback import Origin
from app.services.database import get_session
from app.schemas.nps import NPSCreate, NPSRead, NPSReadList, NPSUpdate
from app.schemas.feedback import FeedbackSummary
from app.usecases.nps import NPSUseCase
from typing import Optional, Literal
from datetime import datetime

router = APIRouter(prefix="/nps", tags=["nps"])

useCase = NPSUseCase()

@router.post("/", response_model=NPSRead)
def create(item: NPSCreate, session: Session = Depends(get_session)):
    return useCase.create_nps(session, item)

@router.get("/", response_model=NPSReadList)
def read(session: Session = Depends(get_session)):
    return useCase.get_nps(session)

@router.get("/summary", response_model=FeedbackSummary)
def read(
    branch_id: Optional[int] = Query(None, description="ID da branch para filtro"),
    origin: Optional[Origin] = Query(None, description="Origem do atendimento para filtro"),
    period: Optional[Literal["day", "week", "month"]] = Query(None, description="Período para filtro"),
    start_date: Optional[datetime] = Query(None, description="Data inicial para filtro"),
    end_date: Optional[datetime] = Query(None, description="Data final para filtro"),
    session: Session = Depends(get_session)
):
    return useCase.get_summary(session, branch_id, origin, period, start_date, end_date)

@router.put("/{id}", response_model=NPSRead)
def update(branch: NPSUpdate, id: int, session: Session = Depends(get_session)):
    return useCase.update_nps(session, id, branch)

@router.delete("/{id}", response_model=None)
def delete(id: int, session: Session = Depends(get_session)):
   return useCase.delete_nps(session, id)