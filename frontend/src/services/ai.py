import requests
from .auth import AuthService
from dotenv import load_dotenv
import os

load_dotenv()

API_URL: str = os.getenv("API_URL", "http://localhost:8000")

class AIService:
    def __init__(self):
        self.api_url = f'{API_URL}/ai'

    def analyze_feedback(self, nps_data: dict, csat_data: dict) -> str:
        body = {"nps_data": nps_data, "csat_data": csat_data}
        return requests.post(f'{self.api_url}/analyze', json=body, headers=AuthService.get_headers()).json()

    def generate_feedback(self, payload: dict):
        return requests.post(f'{self.api_url}/generate', json=payload, headers=AuthService.get_headers())
    