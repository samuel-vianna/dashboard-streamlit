from sqlmodel import SQLModel
from app.schemas.feedback import FeedbackCreate, FeedbackUpdate, FeedbackRead, FeedbackReadList, FeedbackSummary

class NPSCreate(FeedbackCreate):
    pass

class NPSUpdate(FeedbackUpdate):
    pass

class NPSRead(FeedbackRead):
    pass
class NPSReadList(FeedbackReadList):
    pass
