from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.schemas.ai import FeedbackCreateInput, FeedbackCreateResponse
from app.services.database import get_session
from app.usecases.ai import AIUseCase
from typing import Dict

router = APIRouter(prefix="/ai", tags=["ai"])

useCase = AIUseCase()

@router.post("/generate")
def generate_feedback(data: FeedbackCreateInput, session: Session = Depends(get_session)) -> FeedbackCreateResponse:
    return useCase.generate_feedback(session, data)

@router.post("/analyze")
def analyze_feedback(data: Dict, session: Session = Depends(get_session)):
    return useCase.analyze_feedback(session, data)

@router.post("/categorize")
def categorize_feedback(data: Dict, session: Session = Depends(get_session)):
    return useCase.categorize_feedback(session, data)
    
