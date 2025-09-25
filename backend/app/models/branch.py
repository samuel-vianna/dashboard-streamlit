from __future__ import annotations
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.nps import NPSFeedback
    from app.models.csat import CSATFeedback


class Branch(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String, nullable=False, unique=True)) # unique constraint on name

    # nps_feedbacks: List["NPSFeedback"] = Relationship(back_populates="branch")
    # csat_feedbacks: List["CSATFeedback"] = Relationship(back_populates="branch")
