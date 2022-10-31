import json

from ..app.api.routers import drone


def test_create_drone(test_app, monkeypatch):
    test_request_payload = {
        "serial_number": "1",
        "model": "Lightweight",
        "weight_limit": "100.0",
        "battery_capacity": "80",
        "state": "IDLE"
    }
    test_response_payload = {
        "id": 1,
        "serial_number": "1",
        "model": "Lightweight",
        "weight_limit": 100.0,
        "battery_capacity": 80,
        "state": "IDLE"
    }

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(drone, "create_drone", mock_post)

    response = test_app.post(
        "/drones/", data=json.dumps(test_request_payload), )

    assert response.status_code == 200
    assert response.json()['serial_number'] == test_response_payload[
        'serial_number']
    assert response.json()['model'] == test_response_payload['model']
    assert float(response.json()['weight_limit']) == test_response_payload[
        'weight_limit']
    assert int(response.json()['battery_capacity']) == test_response_payload[
        'battery_capacity']
    assert response.json()['state'] == test_response_payload['state']
