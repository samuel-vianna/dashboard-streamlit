from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_users_crud():
    # create
    res = client.post("/users/", json={"username": "u1", "password": "p"})
    assert res.status_code == 200
    data = res.json()
    assert data["username"] == "u1"
    uid = data["id"]

    # list
    res = client.get("/users/")
    assert res.status_code == 200
    assert any(u["id"] == uid for u in res.json())

    # get by id
    res = client.get(f"/users/{uid}")
    assert res.status_code == 200

    # delete
    res = client.delete(f"/users/{uid}")
    assert res.status_code == 200
