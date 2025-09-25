from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.database import get_session
from app.schemas.branch import BranchCreate, BranchRead, BranchUpdate
from app.usecases.branch import (
    create_branch,
    get_branches,
    get_branch_by_id,
    update_branch,
    delete_branch,
)
from typing import List

router = APIRouter(prefix="/branches", tags=["branches"])

@router.post("/", response_model=BranchRead)
def create(branch: BranchCreate, session: Session = Depends(get_session)):
    return create_branch(session, branch)

@router.get("/", response_model=List[BranchRead])
def read(session: Session = Depends(get_session)):
    return get_branches(session)

@router.get("/{id}", response_model=BranchRead)
def read_by_id(id: int, session: Session = Depends(get_session)):
    return get_branch_by_id(session, id)

@router.put("/{id}", response_model=BranchRead)
def update(branch: BranchUpdate, id: int, session: Session = Depends(get_session)):
    return update_branch(session, id, branch)

@router.delete("/{id}", response_model=None)
def delete(id: int, session: Session = Depends(get_session)):
   return delete_branch(session, id)