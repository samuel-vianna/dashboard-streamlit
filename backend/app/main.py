from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.config.database import init_db
from app.controllers import user, branch, nps, csat

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app.include_router(branch.router)
app.include_router(user.router)
app.include_router(nps.router)
app.include_router(csat.router)

@app.get("/ping")
def ping():
    return {"message": "Server is up and running!"}
