# def test_ai_generate(auth_client):
#     client = auth_client
#     payload = {
#             "type": "nps",
#             "amount": 3,
#             "context": "string",
#             "date": "2025-09-29T12:15:10.130Z",
#             "max_time_diff": 0,
#             "branch_id": 0
#         }
#     res = client.post("/ai/generate", json=payload)
#     assert res.status_code == 200
#     data = res.json()
#     assert data["total"] == 3
#     assert isinstance(data["items"], list)


# def test_ai_categorize(auth_client):
#     client = auth_client
#     res = client.post("/ai/categorize", json={})
#     assert res.status_code == 200
#     assert res.json()["message"] == "Feedback categorized successfully."
