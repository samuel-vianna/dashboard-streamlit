from sqlmodel import Session
from app.models.nps import NPSFeedback
from app.schemas.nps import NPSCreate, NPSUpdate

class NPSUseCase:   
    def __init__(self, repository=None):
        self.repository = repository
        
    def create_nps(self, session: Session, data: NPSCreate) -> NPSFeedback:
        item = NPSFeedback(**data.model_dump())
        return self.repository.create(session, item)

    def get_nps(self, session: Session):
        return self.repository.get_all(session)

    def update_nps(self, session: Session, id: int, data: NPSUpdate):
        item = NPSFeedback(**data.model_dump())
        return self.repository.update_by_id(session, id, item)

    def delete_nps(self, session: Session, id: int):
        self.repository.delete(session, id)
        return True
