from sqlmodel import Session
from app.models.branch import Branch
from app.schemas.branch import BranchCreate
class BranchUseCase:
    def __init__(self, repository=None):
        self.repository = repository

    def create_branch(self, session: Session, data: BranchCreate) -> Branch:
        branch = Branch(**data.model_dump())
        return self.repository.create(session, branch)

    def get_branches(self, session: Session):
        return self.repository.get_all(session)

    def get_branch_by_id(self, session: Session, id: int):
        return self.repository.get_by_id(session, id)

    def update_branch(self, session: Session, id: int, data: dict):
        branch = Branch(**data.model_dump())
        return self.repository.update_by_id(session, id, branch)

    def delete_branch(self, session: Session, id: int):
        self.repository.delete(session, id)
        return True
