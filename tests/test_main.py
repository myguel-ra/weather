from weather.app.main import app
from fastapi import testclient

client = testclient(app)

def test_get_temperature():
    response = client.get("/temperature")
    assert response.status_code == 200
    assert response.json() == {"temperature": 30}

def test_get_rain():
    response = client.get("/temperature")
    assert response.status_code == 200
    assert response.json() == {"rain": 30}