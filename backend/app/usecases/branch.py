from sqlmodel import Session
from app.models.branch import Branch
from app.schemas.branch import BranchCreate
from app.repository.branch import BranchRepository

repository = BranchRepository()

def create_branch(session: Session, branch_data: BranchCreate) -> Branch:
    branch = Branch(**branch_data.model_dump())
    return repository.create(session, branch)

def get_branches(session: Session):
    return repository.get_all(session)

def get_branch_by_id(session: Session, id: int):
    return repository.get_by_id(session, id)

def update_branch(session: Session, id: int, data: dict):
    branch = Branch(**data.model_dump())
    return repository.update_by_id(session, id, branch)

def delete_branch(session: Session, id: int):
    repository.delete(session, id)
    return True
