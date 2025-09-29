from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from app.services.database import get_session
from app.models.feedback import Origin
from app.schemas.csat import CSATCreate, CSATRead, CSATReadList, CSATUpdate
from app.schemas.feedback import FeedbackSummary
from app.usecases.csat import CSATUseCase
from typing import Optional, Literal
from datetime import datetime

router = APIRouter(prefix="/csat", tags=["csat"])

useCase = CSATUseCase()

@router.post("/", response_model=CSATRead)
def create(item: CSATCreate, session: Session = Depends(get_session)):
    return useCase.create_csat(session, item)

@router.get("/", response_model=CSATReadList)
def read(session: Session = Depends(get_session)):
    return useCase.get_csats(session)

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

@router.get("/summary/sentiments", response_model=dict[str, int])
def read(session: Session = Depends(get_session)
):
    return useCase.get_sentiments_summary(session)

@router.put("/{id}", response_model=CSATRead)
def update(branch: CSATUpdate, id: int, session: Session = Depends(get_session)):
    return useCase.update_csat(session, id, branch)

@router.delete("/{id}", response_model=None)
def delete(id: int, session: Session = Depends(get_session)):
   return useCase.delete_csat(session, id)