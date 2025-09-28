import requests

API_URL = "http://localhost:8000"

class BranchService:
    def __init__(self):
        self.api_url = f'{API_URL}/branches'
    
    def get_branches(self) -> list[str]:
        return requests.get(f'{self.api_url}').json()