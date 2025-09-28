from __future__ import annotations
from typing import Optional, List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.nps import NPSFeedback
    from app.models.csat import CSATFeedback


class Branch(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, unique=True)

    # npsfeedback: List["NPSFeedback"] = Relationship(back_populates="branch")
    # csatfeedback: List["CSATFeedback"] = Relationship(back_populates="branch")