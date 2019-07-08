import pytest
from app import create_app, db

@pytest.fixture(autouse=True)
def client():
  test_env = create_app('testing')
  client = test_env.test_client()
  return client