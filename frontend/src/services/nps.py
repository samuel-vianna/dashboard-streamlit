import requests

API_URL = "http://localhost:8000"

class NPSService:
    def __init__(self):
        self.api_url = f'{API_URL}/nps'
    
    def get_all(self):
        return requests.get(self.api_url).json()