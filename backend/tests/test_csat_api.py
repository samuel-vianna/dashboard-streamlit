from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_csat_crud():
    # create
    res = client.post("/csat/", json={"score": 3, "comment": "ok"})
    assert res.status_code == 200
    data = res.json()
    assert data["score"] == 3
    csat_id = data["id"]

    # list
    res = client.get("/csat/")
    assert res.status_code == 200
    # assert any(i["id"] == csat_id for i in res.json())

    # update
    res = client.put(f"/csat/{csat_id}", json={"score": 6})
    assert res.status_code == 200
    assert res.json()["score"] == 6

    # delete
    res = client.delete(f"/csat/{csat_id}")
    assert res.status_code == 200


def test_csat_score():
    res = client.post("/csat/", json={"score": 6, "comment": "good"})
    assert res.status_code == 400
    assert res.json()["detail"] == "CSAT score must be between 1 and 5."
    
def test_csat_summary():
    res = client.get("/csat/summary")
    assert res.status_code == 200