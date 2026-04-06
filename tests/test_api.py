from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_prediction_success():
    response = client.post("/predict", json={
        "age": 45,
        "bmi": 28.5,
        "glucose": 150,
        "blood_pressure": 80
    })

    assert response.status_code == 200
    assert "risk" in response.json()


def test_invalid_input():
    response = client.post("/predict", json={
        "age": -1,
        "bmi": 0,
        "glucose": 150,
        "blood_pressure": 80
    })

    assert response.status_code == 422