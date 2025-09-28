from app.models.nps import NPSFeedback
from app.repositories.feedback import FeedbackRepository

scores = {
    "negative": [0, 1, 2, 3, 4, 5, 6],
    "neutral": [7, 8],
    "positive": [9, 10]
}

class NPSRepository(FeedbackRepository[NPSFeedback]):
    def __init__(self):
        super().__init__(NPSFeedback, scores, 'Feedback')