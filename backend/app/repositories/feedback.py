from typing import TypeVar, Type, Optional
from typing import Optional, Literal
from sqlmodel import SQLModel, Session, select, func, case
from app.repositories.base import BaseRepository
from app.models.feedback import ScoreCategories

T = TypeVar("T", bound=SQLModel)

class FeedbackRepository(BaseRepository[T]):
    def __init__(self, model: Type[T], scores: ScoreCategories, name: str = 'Element'):
        self.model = model
        self.name = name
        self.scores = scores

    def get_summary(
        self,
        session: Session,
        branch_id: Optional[int] = None,
        origin: Optional[str] = None,
        group_by: Optional[Literal["day", "week", "month"]] = None,
    ):
        
        # Definir grupo de tempo
        if group_by == "day":
            time_group = func.date_trunc("day", self.model.timestamp).label("period")
        elif group_by == "week":
            time_group = func.date_trunc("week", self.model.timestamp).label("period")
        elif group_by == "month":
            time_group = func.date_trunc("month", self.model.timestamp).label("period")
        else:
            time_group = None
        
        select_columns = [
            self.model.origin,
            func.count().label("total"),
            func.count(case((self.model.score.in_(self.scores["negative"]), 1))).label("negative"),
            func.count(case((self.model.score.in_(self.scores["neutral"]), 1))).label("neutral"),
            func.count(case((self.model.score.in_(self.scores["positive"]), 1))).label("positive"),
        ]
        
        if time_group is not None:
            select_columns.append(time_group)

        query = select(*select_columns)
        
        if branch_id is not None:
            query = query.where(self.model.branch_id == branch_id)

        if origin is not None:
            query = query.where(self.model.origin == origin)
        
        # Agrupamento
        group_by_cols = [self.model.origin]
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