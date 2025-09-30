import sys
import pathlib
import pytest
from fastapi.testclient import TestClient

# ensure project root is on sys.path so `import app` works when pytest runs from backend/
ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.main import app


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def auth_client(client: TestClient):
    # register a test user and obtain token
    username = "testuser"
    password = "testpass"
    res = client.post("/auth/register", json={"username": username, "password": password})
    if res.status_code not in (200, 201):
        # maybe user already exists; try login
        res = client.post("/auth/login", data={"username": username, "password": password})
    else:
        token = res.json()["access_token"]
        client.headers.update({"Authorization": f"Bearer {token}"})
        return client

    # if register returned not ok, try login
    if res.status_code == 200:
        token = res.json()["access_token"]
        client.headers.update({"Authorization": f"Bearer {token}"})
        return client

    pytest.skip("Could not create or login test user")
