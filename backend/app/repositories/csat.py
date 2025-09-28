from sqlmodel import Session, select, func, case
from app.models.csat import CSATFeedback
from app.repositories.base import BaseRepository
from typing import Optional, Literal

class CSATRepository(BaseRepository[CSATFeedback]):
    def __init__(self):
        super().__init__(CSATFeedback, 'Feedback')

    def get_summary(
        self,
        session: Session,
        branch_id: Optional[int] = None,
        origin: Optional[str] = None,
        group_by: Optional[Literal["day", "week", "month"]] = None,
    ):
        
        # Definir grupo de tempo
        if group_by == "day":
            time_group = func.date_trunc("day", CSATFeedback.timestamp).label("period")
        elif group_by == "week":
            time_group = func.date_trunc("week", CSATFeedback.timestamp).label("period")
        elif group_by == "month":
            time_group = func.date_trunc("month", CSATFeedback.timestamp).label("period")
        else:
            time_group = None
        
        select_columns = [
            CSATFeedback.origin,
            func.count().label("total"),
            func.count(case((CSATFeedback.score.between(1, 2), 1))).label("negative"),
            func.count(case((CSATFeedback.score.in_([3]), 1))).label("neutral"),
            func.count(case((CSATFeedback.score.in_([4, 5]), 1))).label("positive"),
        ]
        
        if time_group is not None:
            select_columns.append(time_group)

        query = select(*select_columns)
        
        if branch_id is not None:
            query = query.where(CSATFeedback.branch_id == branch_id)

        if origin is not None:
            query = query.where(CSATFeedback.origin == origin)
        
        # Agrupamento
        group_by_cols = [CSATFeedback.origin]
        if time_group is not None:
            group_by_cols.append(time_group)

        query = query.group_by(*group_by_cols)
        
        results = session.exec(query).all()
        return [
            {
                "origin": r.origin,
                "period": r.period if r.period else None,
                "total": r.total,
                "negative": r.negative,
                "neutral": r.neutral,
                "positive": r.positive,
            }
            for r in results
        ]