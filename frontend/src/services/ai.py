import requests

API_URL = "http://localhost:8000"

class AIService:
    def __init__(self):
        self.api_url = f'{API_URL}'
    
    def generate_feedback(self, nps_data: dict, csat_data: dict) -> str:
        body = {"nps_data": nps_data, "csat_data": csat_data}
        return requests.post(f'{self.api_url}/ai/analyze', json=body).json()
    