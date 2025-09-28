from sqlmodel import Session, select, func, case
from app.models.csat import CSATFeedback
from app.repositories.base import BaseRepository
from typing import Optional

class CSATRepository(BaseRepository[CSATFeedback]):
    def __init__(self):
        super().__init__(CSATFeedback, 'Feedback')

    def get_summary(self, session: Session, branch_id: Optional[int] = None, origin: Optional[str] = None):
        query = select(
            CSATFeedback.origin,
            func.count().label("total"),
            func.count(case((CSATFeedback.score.between(1, 2), 1))).label("negative"),
            func.count(case((CSATFeedback.score.in_([3]), 1))).label("neutral"),
            func.count(case((CSATFeedback.score.in_([4, 5]), 1))).label("positive"),
        )
        
        if branch_id is not None:
            query = query.where(CSATFeedback.branch_id == branch_id)

        if origin is not None:
            query = query.where(CSATFeedback.origin == origin)
        
        query = query.group_by(CSATFeedback.origin)
        
        results = session.exec(query).all()

        return [
            {
                "origin": r.origin,
                "total": r.total,
                "negative": r.negative,
                "neutral": r.neutral,
                "positive": r.positive,
            }
            for r in results
        ]