from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_nps_crud():
    # create
    res = client.post("/nps/", json={"score": 8, "comment": "good"})
    assert res.status_code == 200
    data = res.json()
    assert data["score"] == 8
    nps_id = data["id"]

    # list
    res = client.get("/nps/")
    assert res.status_code == 200
    assert any(i["id"] == nps_id for i in res.json())

    # update
    res = client.put(f"/nps/{nps_id}", json={"score": 9})
    assert res.status_code == 200
    assert res.json()["score"] == 9

    # delete
    res = client.delete(f"/nps/{nps_id}")
    assert res.status_code == 200
