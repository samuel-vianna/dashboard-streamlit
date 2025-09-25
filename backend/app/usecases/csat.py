from sqlmodel import Session
from fastapi import HTTPException
from app.models.csat import CSATFeedback
from app.schemas.csat import CSATCreate
from app.repositories.csat import CSATRepository
class CSATUseCase:
    def __init__(self):
        self.repository = CSATRepository()

    def create_csat(self, session: Session, data: CSATCreate) -> CSATFeedback:
        if not 1 <= data.score <= 5:
            raise HTTPException(status_code=400, detail="CSAT score must be between 1 and 5.")
        csat = CSATFeedback(**data.model_dump())
        return self.repository.create(session, csat)

    def get_csats(self, session: Session):
        return self.repository.get_all(session)

    def get_csat_by_id(self, session: Session, id: int):
        return self.repository.get_by_id(session, id)

    def update_csat(self, session: Session, id: int, data: dict):
        csat = CSATFeedback(**data.model_dump())
        return self.repository.update_by_id(session, id, csat)

    def delete_csat(self, session: Session, id: int):
        self.repository.delete(session, id)
        return True
