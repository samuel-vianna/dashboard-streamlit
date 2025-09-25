from sqlmodel import Session, select, func, case
from app.models.nps import NPSFeedback
from app.repositories.base import BaseRepository
from typing import Optional

class NPSRepository(BaseRepository[NPSFeedback]):
    def __init__(self):
        super().__init__(NPSFeedback, 'Feedback')

    def get_summary(self, session: Session, branch_id: Optional[int] = None, origin: Optional[str] = None):
        query = select(
            NPSFeedback.origin,
            func.count().label("total"),
            func.count(case((NPSFeedback.score.between(0, 6), 1))).label("negative"),
            func.count(case((NPSFeedback.score.in_([7, 8]), 1))).label("neutral"),
            func.count(case((NPSFeedback.score.in_([9, 10]), 1))).label("positive"),
        )
        
        if branch_id is not None:
            query = query.where(NPSFeedback.branch_id == branch_id)

        if origin is not None:
            query = query.where(NPSFeedback.origin == origin)
        
        query = query.group_by(NPSFeedback.origin)
        
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