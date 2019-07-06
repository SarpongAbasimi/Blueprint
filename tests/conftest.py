import pytest
from app import current_app

@pytest.fixture()
def client():
  current_app().config['Testing'] = True
  client = current_app().test_client()
  return client