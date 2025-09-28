from app.models.csat import CSATFeedback
from app.repositories.feedback import FeedbackRepository

scores = {
    "negative": [1, 2],
    "neutral": [3],
    "positive": [4, 5]
}
class CSATRepository(FeedbackRepository[CSATFeedback]):
    def __init__(self):
        super().__init__(CSATFeedback, scores, 'Feedback')
