from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_csat_crud():
    # create
    res = client.post("/csat/", json={"score": 7, "comment": "ok"})
    assert res.status_code == 200
    data = res.json()
    assert data["score"] == 7
    csat_id = data["id"]

    # list
    res = client.get("/csat/")
    assert res.status_code == 200
    assert any(i["id"] == csat_id for i in res.json())

    # update
    res = client.put(f"/csat/{csat_id}", json={"score": 6})
    assert res.status_code == 200
    assert res.json()["score"] == 6

    # delete
    res = client.delete(f"/csat/{csat_id}")
    assert res.status_code == 200
