from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.schemas.csat import CSATCreate, CSATUpdate
from app.config.database import get_session
from app.repository.csat import CSATRepository
from app.usecases.csat import CSATUseCase

router = APIRouter(prefix="/csat", tags=["csat"])

repository = CSATRepository()
useCase = CSATUseCase(repository)

@router.post("/", response_model=dict)
def create(csat_data: CSATCreate, session: Session = Depends(get_session)):
    try:
        csat = useCase.create_csat(session, csat_data)
        return {"id": csat.id, "score": csat.score}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list)
def list_csats(session: Session = Depends(get_session)):
    return useCase.get_csats(session)

@router.get("/{id}", response_model=dict)
def retrieve(id: int, session: Session = Depends(get_session)):
    csat = useCase.get_csat_by_id(session, id)
    return {"id": csat.id, "score": csat.score}

@router.put("/{id}", response_model=dict)
def update(id: int, data: CSATUpdate, session: Session = Depends(get_session)):
    csat = useCase.update_csat(session, id, data)
    return {"id": csat.id, "score": csat.score}

@router.delete("/{id}")
def delete(id: int, session: Session = Depends(get_session)):
    useCase.delete_csat(session, id)
    return {"message": "deleted"}