import pytest
from app import current_app, db

@pytest.fixture(autouse=True)
def client():
  test_env = current_app('testing')
  client = test_env.test_client()
  return client