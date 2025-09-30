from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.services.database.database import init_db
from app.controllers import user, branch, nps, csat, ai, auth
from dotenv import load_dotenv
from app.services.jobs.categorize import start_categorize_scheduler, stop_categorize_scheduler
from app.services.jobs.generate_comments import start_generate_scheduler, stop_generate_scheduler
from scripts.seed import seed
from scripts.seed_feedback import seed_feedback

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # initialize DB
    await init_db()
    seed()
    seed_feedback()
    # start scheduler (if available)
    start_categorize_scheduler()
    start_generate_scheduler()
    yield
    # stop scheduler on shutdown
    stop_categorize_scheduler()
    stop_generate_scheduler()


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
