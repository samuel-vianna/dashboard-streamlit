from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.branch import BranchCreate, BranchUpdate
from app.config.database import get_session
from app.repository.branch import BranchRepository
from app.usecases.branch import BranchUseCase

router = APIRouter(prefix="/branches", tags=["branches"])

repository = BranchRepository()
useCase = BranchUseCase(repository)


@router.post("/", response_model=dict)
def create(branch_data: BranchCreate, session: Session = Depends(get_session)):
    try:
        branch = useCase.create_branch(session, branch_data)
        return {"id": branch.id, "name": branch.name}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list)
def list_branches(session: Session = Depends(get_session)):
    return useCase.get_branches(session)


@router.get("/{id}", response_model=dict)
def retrieve(id: int, session: Session = Depends(get_session)):
    branch = useCase.get_branch_by_id(session, id)
    return {"id": branch.id, "name": branch.name}


@router.put("/{id}", response_model=dict)
def update(id: int, data: BranchUpdate, session: Session = Depends(get_session)):
    branch = useCase.update_branch(session, id, data)
    return {"id": branch.id, "name": branch.name}


@router.delete("/{id}")
def delete(id: int, session: Session = Depends(get_session)):
    useCase.delete_branch(session, id)
    return {"message": "deleted"}