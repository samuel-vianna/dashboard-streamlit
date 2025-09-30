from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.schemas.ai import FeedbackCreateInput, FeedbackCreateResponse, AIAnalyzeInput
from app.services.database import get_session
from app.usecases.ai import AIUseCase
from typing import Dict
from app.utils.security import get_current_user

router = APIRouter(prefix="/ai", tags=["ai"])

useCase = AIUseCase()

@router.post("/generate")
def generate_feedback(data: FeedbackCreateInput, session: Session = Depends(get_session), current_user=Depends(get_current_user)) -> FeedbackCreateResponse:
    return useCase.generate_feedback(session, data)

@router.post("/analyze")
def analyze_feedback(data: AIAnalyzeInput, session: Session = Depends(get_session), current_user=Depends(get_current_user)):
    return useCase.analyze_feedback(data)
