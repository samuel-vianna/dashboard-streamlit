from sqlmodel import Session, select, func, case
from app.models.nps import NPSFeedback
from app.repositories.base import BaseRepository
from typing import Optional
from typing import Optional, Literal

class NPSRepository(BaseRepository[NPSFeedback]):
    def __init__(self):
        super().__init__(NPSFeedback, 'Feedback')

    def get_summary(
        self,
        session: Session,
        branch_id: Optional[int] = None,
        origin: Optional[str] = None,
        group_by: Optional[Literal["day", "week", "month"]] = None,
    ):
        
        # Definir grupo de tempo
        if group_by == "day":
            time_group = func.date_trunc("day", NPSFeedback.timestamp).label("period")
        elif group_by == "week":
            time_group = func.date_trunc("week", NPSFeedback.timestamp).label("period")
        elif group_by == "month":
            time_group = func.date_trunc("month", NPSFeedback.timestamp).label("period")
        else:
            time_group = None
        
        select_columns = [
            NPSFeedback.origin,
            func.count().label("total"),
            func.count(case((NPSFeedback.score.between(0, 6), 1))).label("negative"),
            func.count(case((NPSFeedback.score.in_([7,8]), 1))).label("neutral"),
            func.count(case((NPSFeedback.score.in_([9, 10]), 1))).label("positive"),
        ]
        
        if time_group is not None:
            select_columns.append(time_group)

        query = select(*select_columns)
        
        if branch_id is not None:
            query = query.where(NPSFeedback.branch_id == branch_id)

        if origin is not None:
            query = query.where(NPSFeedback.origin == origin)
        
        # Agrupamento
        group_by_cols = [NPSFeedback.origin]
        if time_group is not None:
            group_by_cols.append(time_group)

        query = query.group_by(*group_by_cols)
        
        results = session.exec(query).all()
        return [
            {
                "origin": r.origin,
                "period": r.period if group_by else None,
                "total": r.total,
                "negative": r.negative,
                "neutral": r.neutral,
                "positive": r.positive,
            }
            for r in results
        ]