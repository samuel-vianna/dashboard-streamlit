from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_branches_crud():
    # create
    res = client.post("/branches/", json={"name": "Loja Test"})
    assert res.status_code == 200
    data = res.json()
    assert data["name"] == "Loja Test"
    branch_id = data["id"]

    # list
    res = client.get("/branches/")
    assert res.status_code == 200
    assert any(b["id"] == branch_id for b in res.json())

    # get by id
    res = client.get(f"/branches/{branch_id}")
    assert res.status_code == 200

    # update
    res = client.put(f"/branches/{branch_id}", json={"name": "Loja Test Updated"})
    assert res.status_code == 200
    assert res.json()["name"] == "Loja Test Updated"

    # delete
    res = client.delete(f"/branches/{branch_id}")
    assert res.status_code == 200
