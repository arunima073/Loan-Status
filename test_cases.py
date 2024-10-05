#stimulating realtime environment
from predict import app
import pytest

@pytest.fixture
def client():
  return app.test_client()

def test_ping(client):
  resp=client.get('/ping')
  assert resp.status_code==200
  assert resp.json=={"MESSAGE":"Hi,I am Pinging....!!!!!"}


def test_predict(client):
  test_data={
    "Gender": "Female",
    "Married": "unmarried",
    "ApplicantIncome": 5000000,
    "Credit_History": "Cleared Debts",
    "LoanAmount": 5000
  }

  resp=client.post('/predict',json=test_data)
  assert resp.status_code==200
  assert resp.json=={"loan approve status": "Approved"}

