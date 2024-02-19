from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_temperature():
    # Test case 1: Valid input
    response = client.get("/temperature", params={"city": "lisbon", "days": 3})
    assert response.status_code == 200
    assert response.json() == {"temperature": 25.5}
    # Test case 2: Invalid input (simulate a specific exception)
    response = client.get("/temperature", params={"city": "UndefinedCity", "days": 3})
    assert response.status_code == 400


def test_will_rain():
    # Test case 3: Valid input
    response = client.get("/rain", params={"city": "lisbon", "days": 3})
    assert response.status_code == 200
    assert response.json() == {"will_rain": True}
    # Test case 4: Invalid input (simulate a specific exception)
    response = client.get("/rain", params={"city": "UndefinedCity", "days": 3})
    assert response.status_code == 400
