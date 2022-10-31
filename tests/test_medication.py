import json

from app.api.routers import medication


def test_create_drone(test_app, monkeypatch):
    test_request_payload = {
        "name": "Dipi",
        "weight": "15.5",
        "code": "AB12",
        "image": "http://musala.com/static/1.jpg"
    }
    test_response_payload = {
        "id": 1,
        "name": "Dipi",
        "weight": 15.5,
        "code": "AB12",
        "image": "http://musala.com/static/1.jpg"
    }

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(medication, "create_medication", mock_post)

    response = test_app.post(
        "/medications/", data=json.dumps(test_request_payload))

    assert response.status_code == 200
    assert response.json()['name'] == test_response_payload['name']
    assert float(response.json()['weight']) == test_response_payload['weight']
    assert response.json()['code'] == test_response_payload['code']
    assert response.json()['image'] == test_response_payload['image']
