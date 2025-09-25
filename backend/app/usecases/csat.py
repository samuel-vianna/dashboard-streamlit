from sqlmodel import Session
from fastapi import HTTPException
from typing import Optional
from app.models.csat import CSATFeedback
from app.schemas.csat import CSATCreate, CSATReadList
from app.repositories.csat import CSATRepository
from app.repositories.branch import BranchRepository
from app.utils.calculate_csat import calculate_csat
class CSATUseCase:
    def __init__(self):
        self.repository = CSATRepository()
        self.branch_repository = BranchRepository()

    def create_csat(self, session: Session, data: CSATCreate) -> CSATFeedback:
        if data.branch_id is not None:
            branch = self.branch_repository.get_by_id(session, data.branch_id)
            if branch is None:
                raise HTTPException(status_code=400, detail=f"Branch {data.branch_id} not found.")
        
        if not 1 <= data.score <= 5:
            raise HTTPException(status_code=400, detail="CSAT score must be between 1 and 5.")
        csat = CSATFeedback(**data.model_dump())
        return self.repository.create(session, csat)

    def get_csats(self, session: Session) -> CSATReadList:
        items = self.repository.get_all(session)
        return {"total": len(items), "items": items}

    def get_csat_by_id(self, session: Session, id: int):
        return self.repository.get_by_id(session, id)

    def update_csat(self, session: Session, id: int, data: dict):
        csat = CSATFeedback(**data.model_dump())
        return self.repository.update_by_id(session, id, csat)

    def delete_csat(self, session: Session, id: int):
        self.repository.delete(session, id)
        return True

    def get_summary(self, session: Session, branch_id: Optional[int] = None, origin: Optional[str] = None):
        results = self.repository.get_summary(session, branch_id, origin)
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
            "details": [{**r, "score": calculate_csat(r)} for r in results]
        }
        
        score = calculate_csat(summary)
        return {**summary, "score": score}
        