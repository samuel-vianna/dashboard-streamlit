from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.services.database.database import get_session
from app.schemas.user import UserCreate, LoginInput, Token
from app.usecases.user import UserUseCase

router = APIRouter(prefix="/auth", tags=["auth"])

useCase = UserUseCase()

@router.post("/register", response_model=Token)
def register(user: UserCreate, session: Session = Depends(get_session)):
    # check existing
    existing = useCase.repository.get_by_username(session, user.username)
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    created = useCase.create_user(session, user)
    token = useCase.create_token_for_user(created)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/login", response_model=Token)
def login(data: LoginInput, session: Session = Depends(get_session)):
    user = useCase.authenticate_user(session, data.username, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = useCase.create_token_for_user(user)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/logout")
def logout():
    # stateless JWT: client should drop token. Keep endpoint for parity.
    return {"message": "logged out"}
