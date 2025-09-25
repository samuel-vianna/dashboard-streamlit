from sqlmodel import Session
from fastapi import HTTPException
from app.models.nps import NPSFeedback
from app.schemas.nps import NPSCreate, NPSUpdate

class NPSUseCase:   
    def __init__(self, repository=None):
        self.repository = repository
        
    def create_nps(self, session: Session, data: NPSCreate) -> NPSFeedback:
        if not 0 <= data.score <= 10:
            raise HTTPException(status_code=400, detail="NPS score must be between 0 and 10.")
        nps = NPSFeedback(**data.model_dump())
        return self.repository.create(session, nps)

    def get_nps(self, session: Session):
        return self.repository.get_all(session)

    def update_nps(self, session: Session, id: int, data: NPSUpdate):
        nps = NPSFeedback(**data.model_dump())
        return self.repository.update_by_id(session, id, nps)

    def delete_nps(self, session: Session, id: int):
        self.repository.delete(session, id)
        return True
