from typing import Type, Optional, List
from sqlmodel import Session, select
from app.models.nps import NPSFeedback
from app.repository.base import BaseRepository


class NPSRepository(BaseRepository[NPSFeedback]):
    def __init__(self):
        super().__init__(NPSFeedback, 'Feedback')

