from sqlmodel import Session
from fastapi import HTTPException
from typing import Optional, Literal
from app.models.nps import NPSFeedback
from app.schemas.nps import NPSCreate, NPSReadList, NPSUpdate
from app.repositories.nps import NPSRepository
from app.repositories.branch import BranchRepository
from app.utils.calculate_nps import calculate_nps
from datetime import datetime

class NPSUseCase:   
    def __init__(self):
        self.repository = NPSRepository()
        self.branch_repository = BranchRepository()
        
    def create_nps(self, session: Session, data: NPSCreate) -> NPSFeedback:
        if data.branch_id is not None:
            branch = self.branch_repository.get_by_id(session, data.branch_id)
            if branch is None:
                raise HTTPException(status_code=400, detail=f"Branch {data.branch_id} not found.")
        
        if not 0 <= data.score <= 10:
            raise HTTPException(status_code=400, detail="NPS score must be between 0 and 10.")
        nps = NPSFeedback(**data.model_dump())
        return self.repository.create(session, nps)

    def get_nps(self, session: Session) -> NPSReadList:
        items = self.repository.get_all(session)
        return {"total": len(items), "items": items}

    def update_nps(self, session: Session, id: int, data: NPSUpdate):
        nps = NPSFeedback(**data.model_dump())
        return self.repository.update_by_id(session, id, nps)

    def delete_nps(self, session: Session, id: int):
        self.repository.delete(session, id)
        return True

    def get_summary(
        self,
        session: Session,
        branch_id: Optional[int] = None,
        origin: Optional[str] = None,
        period: Optional[Literal["day", "week", "month"]] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
        ):
        results = self.repository.get_summary(session, branch_id, origin, period, start_date, end_date)
        
        # calculate total summing all origins
        total = sum(item["total"] for item in results)
        positive = sum(item["positive"] for item in results)
        negative = sum(item["negative"] for item in results)
        neutral = sum(item["neutral"] for item in results)
        summary = {
            "total": total,
            "positive": positive,
            "negative": negative,
            "neutral": neutral,
            "details": [{**r, "score": calculate_nps(r)} for r in results]
        }
        
        score = calculate_nps(summary)
        return {**summary, "score": score}
        