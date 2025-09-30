import requests
from .auth import AuthService

API_URL = "http://localhost:8000"


class BranchService:
    def __init__(self):
        self.api_url = f'{API_URL}/branches'

    def create_branch(self, name: str):
        return requests.post(f'{self.api_url}', json={"name": name}, headers=AuthService.get_headers())

    def get_branches(self) -> list[str]:
        return requests.get(f'{self.api_url}', headers=AuthService.get_headers()).json()
    
    def get_origins(self) -> list[str]:
        return [
            "site",
            "app",
            "telefone",
            "email",
            "chat",
            "presencial"
        ]
    