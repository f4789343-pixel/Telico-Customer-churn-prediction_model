import pytest
from fastapi.testclient import TestClient
from api import app
from unittest.mock import patch
import psycopg

client = TestClient(app)

def test_health():
  response = client.get("/health")
  assert response.status_code == 200

def test_missing_input():
  response = client.post('/predict', json={})
  assert response.status_code == 422

valid_payload = {
  "gender": "Female",
  "SeniorCitizen": 1,
  "Partner": "Yes",
  "Dependents": "Yes",
  "tenure": 0,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "Contract": "Month-to-month"
}

def test_validation():
   response = client.post('/predict',json=valid_payload)
   assert response.status_code == 200
   assert "prediction" in response.json()


def test_prediction_history():
  before = client.get('/predictions').json()
  before_count = len(before['predictions'])
  response = client.post('/predict',json=valid_payload)
  assert response.status_code == 200

  after = client.get('/predictions').json()
  after_count = len(after['predictions'])
  assert after_count == before_count + 1

def test_health_database_available():
  with patch('api.pool.connection', side_effect=psycopg.OperationalError):
    response = client.get('/health')
  assert response.status_code == 503