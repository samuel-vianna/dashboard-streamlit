from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.schemas.branch import BranchCreate, BranchRead, BranchUpdate
from app.config.database import get_session
from app.repositories.branch import BranchRepository
from app.usecases.branch import BranchUseCase
from typing import List

router = APIRouter(prefix="/branches", tags=["branches"])

repository = BranchRepository()
useCase = BranchUseCase(repository)

@router.post("/", response_model=BranchRead)
def create(item: BranchCreate, session: Session = Depends(get_session)):
    return useCase.create_branch(session, item)

@router.get("/", response_model=List[BranchRead])
def read(session: Session = Depends(get_session)):
    return useCase.get_branches(session)

@router.get("/{id}", response_model=BranchRead)
def read_by_id(id: int, session: Session = Depends(get_session)):
    return useCase.get_branch_by_id(session, id)
    
@router.put("/{id}", response_model=BranchRead)
def update(id: int, data: BranchUpdate, session: Session = Depends(get_session)):
    return useCase.update_branch(session, id, data)

@router.delete("/{id}")
def delete(id: int, session: Session = Depends(get_session)):
    return useCase.delete_branch(session, id)