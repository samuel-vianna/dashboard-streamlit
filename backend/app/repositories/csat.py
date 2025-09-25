from typing import Type, Optional, List
from sqlmodel import Session, select
from app.models.csat import CSATFeedback
from app.repositories.base import BaseRepository


class CSATRepository(BaseRepository[CSATFeedback]):
    def __init__(self):
        super().__init__(CSATFeedback, 'Feedback')

