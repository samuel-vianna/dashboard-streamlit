from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.schemas.ai import FeedbackCreate
from app.config.database import get_session
# from app.repositories.branch import BranchRepository
from app.usecases.ai import AIUseCase

router = APIRouter(prefix="/ai", tags=["ai"])

repository = None
useCase = AIUseCase()


@router.post("/generate")
def generate_feedback(data: FeedbackCreate, session: Session = Depends(get_session)):
    return useCase.generate_feedback(session, data)
    

@router.post("/analyze")
def analyze_feedback(data: list, session: Session = Depends(get_session)):
    return useCase.analyze_feedback(session, data)
    

@router.post("/categorize")
def categorize_feedback(data: list, session: Session = Depends(get_session)):
    return useCase.categorize_feedback(session, data)
    
