from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.services.database.database import init_db
from app.controllers import user, branch, nps, csat, ai, auth
from dotenv import load_dotenv
from app.services.scheduler import start_scheduler, stop_scheduler

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # initialize DB
    await init_db()
    # start scheduler (if available)
    start_scheduler()
    yield
    # stop scheduler on shutdown
    stop_scheduler()


app = FastAPI(lifespan=lifespan)

app.include_router(ai.router)
app.include_router(branch.router)
app.include_router(user.router)
app.include_router(nps.router)
app.include_router(csat.router)
app.include_router(auth.router)

@app.get("/ping")
def ping():
    return {"message": "Server is up and running!"}
