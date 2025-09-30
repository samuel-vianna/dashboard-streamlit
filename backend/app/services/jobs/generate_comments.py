import logging
from typing import Optional
from app.schemas.ai import FeedbackCreateInput
import os

try:
    from apscheduler.schedulers.background import BackgroundScheduler
    from apscheduler.triggers.interval import IntervalTrigger
except Exception:
    BackgroundScheduler = None

from app.usecases.ai import AIUseCase
from app.services.database.database import engine
from sqlmodel import Session
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

scheduler: Optional[BackgroundScheduler] = None


def _run_generate():
    try:
        logger.info("Running generate_feedback job")
        with Session(engine) as session:
            usecase = AIUseCase()
            
            now = datetime.now(timezone.utc) 
            iso_format = now.isoformat(timespec="milliseconds").replace("+00:00", "Z")
            
            data_nps = FeedbackCreateInput(
                type="nps",
                amount=50,
                context="comentários variados",
                date=iso_format,
                max_time_diff=3,
                branch_id=1
            )
            
            data_csat = FeedbackCreateInput(
                type="csat",
                amount=50,
                context="comentários variados",
                date=iso_format,
                max_time_diff=3,
                branch_id=1
            )
            
            
            res_nps = usecase.generate_feedback(session, data_nps)
            res_csat = usecase.generate_feedback(session, data_csat)
            logger.info(f"Comments generated successfully!")
    except Exception as e:
        logger.exception(f"Error running generate job: {e}")


def start_generate_scheduler():
    global scheduler
    if BackgroundScheduler is None:
        logger.warning("APScheduler not installed; scheduler will not run.")
        return
    if scheduler is not None:
        return

    scheduler = BackgroundScheduler(daemon=True)

    if scheduler.get_job("generate_feedback"):
        scheduler.remove_job("generate_feedback")

    scheduler_interval = os.getenv("SCHEDULER_INTERVAL", 1)
    scheduler.add_job(
        _run_generate,
        IntervalTrigger(minutes=scheduler_interval),
        id="generate_feedback",
        replace_existing=True
    )
    scheduler.start()
    logger.info(f"Scheduler started — job 'generate_feedback' running every {scheduler_interval} minute")


def stop_generate_scheduler():
    global scheduler
    if scheduler is None:
        return
    scheduler.shutdown(wait=False)
    scheduler = None
    logger.info("Scheduler stopped")
