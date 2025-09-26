import requests
from typing import TypedDict, Any

API_URL = "http://localhost:8000"

class SummaryData(TypedDict):
    total: int
    negative: int
    neutral: int
    positive: int
    score: float
    details: list[dict[str, Any]]

class FeedbackService:
    def __init__(self, endpoint: str):
        self.api_url = f'{API_URL}/{endpoint}'
    
    def get_all(self):
        return requests.get(self.api_url).json()
    
    def get_summary(self) -> SummaryData:
        return requests.get(f'{self.api_url}/summary').json()