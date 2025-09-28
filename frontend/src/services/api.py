import requests

API_URL = "http://localhost:8000"

def post_generate(prompt):
    return requests.post(f"{API_URL}/ai/generate", json={"input": prompt}).json()

def get_dashboard_data():
    return requests.get(f"{API_URL}/dashboard").json()
