from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship
from app.models.feedback import Feedback
from sqlalchemy.orm import Mapped

if TYPE_CHECKING:
    from app.models.branch import Branch


class NPSFeedback(Feedback, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    branch_id: Optional[int] = Field(default=None, foreign_key="branch.id")
    # branch: Optional[Branch] = Relationship(back_populates="npsfeedback")