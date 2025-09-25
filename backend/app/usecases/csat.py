from sqlmodel import Session
from app.models.csat import CSATFeedback
from app.schemas.csat import CSATCreate, CSATUpdate
from app.repository.csat import CSATRepository

repository = CSATRepository()

def create_csat(session: Session, data: CSATCreate) -> CSATFeedback:
    item = CSATFeedback(**data.model_dump())
    return repository.create(session, item)

def get_csats(session: Session):
    return repository.get_all(session)

def update_csat(session: Session, id: int, data: CSATUpdate):
    item = CSATFeedback(**data.model_dump())
    return repository.update_by_id(session, id, item)

def delete_csat(session: Session, id: int):
    repository.delete(session, id)
    return True
