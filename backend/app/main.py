from fastapi import FastAPI
from app.config.database import init_db
from app.controllers import user

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI in Docker!"}
