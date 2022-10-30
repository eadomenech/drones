import json

from ..app.api.rounters import drone


def test_create_drone(test_app, monkeypatch):
    test_request_payload = {
        "serial_number": "123456",
        "model": "Lightweight",
        "weight_limit": "100.0",
        "battery_capacity": "80",
        "state": "idle"
    }
    test_response_payload = {
        "id": 1,
        "serial_number": "123456",
        "model": "Lightweight",
        "weight_limit": "100.0",
        "battery_capacity": "80",
        "state": "idle"
    }

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(drone, "create_drone", mock_post)

    response = test_app.post(
        "/drones/", data=json.dumps(test_request_payload), )

    assert response.status_code == 201
    # assert response.json() == test_response_payload
