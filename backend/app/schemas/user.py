from typing import Optional
from sqlmodel import SQLModel

class UserCreate(SQLModel):
    username: str
    password: str

class UserRead(SQLModel):
    id: int
    username: str


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


class LoginInput(SQLModel):
    username: str
    password: str
