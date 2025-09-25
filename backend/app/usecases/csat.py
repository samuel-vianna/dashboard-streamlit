from sqlmodel import Session
from app.models.csat import CSATFeedback
from app.schemas.csat import CSATCreate

class CSATUseCase:
    def __init__(self, repository=None):
        self.repository = repository

    def create_csat(self, session: Session, csat_data: CSATCreate) -> CSATFeedback:
        csat = CSATFeedback(**csat_data.model_dump())
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
