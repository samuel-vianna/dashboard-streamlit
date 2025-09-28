import requests
from typing import TypedDict, Optional

API_URL = "http://localhost:8000"


class SummaryInfo(TypedDict):
    total: int
    negative: int
    neutral: int
    positive: int
    score: float

class SummaryDetails(SummaryInfo): 
    origin: str
    
class SummaryData(SummaryInfo):
    details: list[SummaryDetails]

class FeedbackService:
    def __init__(self, endpoint: str):
        self.api_url = f'{API_URL}/{endpoint}'
    
    def get_all(self):
        return requests.get(self.api_url).json()
    
    def get_summary(self, branch_id: Optional[int] = None) -> SummaryData:
        return requests.get(f'{self.api_url}/summary', params={"branch_id": branch_id}).json()
    
    def get_branches(self) -> list[str]:
        return requests.get(f'{self.api_url}/branches').json()