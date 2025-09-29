import requests
from typing import TypedDict, Optional, Literal
from datetime import datetime

API_URL = "http://localhost:8000"

class SummaryInfo(TypedDict):
    total: int
    negative: int
    neutral: int
    positive: int
    score: float

class SummaryDetails(SummaryInfo): 
    origin: str
    period: Optional[datetime]
    
class SummaryData(SummaryInfo):
    details: list[SummaryDetails]

class FeedbackService:
    def __init__(self, endpoint: str):
        self.api_url = f'{API_URL}/{endpoint}'
    
    def get_all(self):
        return requests.get(self.api_url).json()
    
    def get_sentiments(self):
        return requests.get(f'{self.api_url}/summary/sentiments').json()
    
    def get_summary(
        self,
        branch_id: Optional[int] = None,
        origin: Optional[str] = None,
        period: Optional[Literal["day", "week", "month"]] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
        ) -> SummaryData:
        params = {
            "branch_id": branch_id,
            "origin": origin,
            "period": period,
            "start_date": start_date,
            "end_date": end_date
        }
        return requests.get(f'{self.api_url}/summary', params=params).json()
    
    def get_branches(self) -> list[str]:
        return requests.get(f'{self.api_url}/branches').json()