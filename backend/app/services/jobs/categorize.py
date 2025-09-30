import logging
from typing import Optional
import os

try:
    from apscheduler.schedulers.background import BackgroundScheduler
    from apscheduler.triggers.interval import IntervalTrigger
except Exception:
    BackgroundScheduler = None

from app.usecases.ai import AIUseCase
from app.services.database.database import engine
from sqlmodel import Session

logger = logging.getLogger(__name__)

scheduler: Optional[BackgroundScheduler] = None


def _run_categorize():
    try:
        logger.info("Running categorize_feedback job")
        with Session(engine) as session:
            usecase = AIUseCase()
            res = usecase.categorize_feedback(session)
            logger.info(f"Categorize job result: {res}")
    except Exception as e:
        logger.exception(f"Error running categorize job: {e}")


def start_categorize_scheduler():
    global scheduler
    if BackgroundScheduler is None:
        logger.warning("APScheduler not installed; scheduler will not run.")
        return
    if scheduler is not None:
        return

    scheduler = BackgroundScheduler(daemon=True)

    if scheduler.get_job("categorize_feedback"):
        scheduler.remove_job("categorize_feedback")

    scheduler_interval = os.getenv("SCHEDULER_INTERVAL", 1)
    scheduler.add_job(
        _run_categorize,
        IntervalTrigger(minutes=scheduler_interval),
        id="categorize_feedback",
        replace_existing=True
    )
    scheduler.start()
    logger.info(f"Scheduler started — job 'categorize_feedback' running every {scheduler_interval} minute")


def stop_categorize_scheduler():
    global scheduler
    if scheduler is None:
        return
    scheduler.shutdown(wait=False)
    scheduler = None
    logger.info("Scheduler stopped")
