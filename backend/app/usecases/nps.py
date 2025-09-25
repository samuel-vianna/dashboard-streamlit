from sqlmodel import Session
from app.models.nps import NPSFeedback
from app.schemas.nps import NPSCreate, NPSUpdate
from app.repository.nps import NPSRepository

repository = NPSRepository()

def create_nps(session: Session, data: NPSCreate) -> NPSFeedback:
    item = NPSFeedback(**data.model_dump())
    return repository.create(session, item)

def get_nps(session: Session):
    return repository.get_all(session)

def update_nps(session: Session, id: int, data: NPSUpdate):
    item = NPSFeedback(**data.model_dump())
    return repository.update_by_id(session, id, item)

def delete_nps(session: Session, id: int):
    repository.delete(session, id)
    return True
