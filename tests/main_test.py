import pytest
from app import current_app

@pytest.fixture()
def client():
  current_app().config['Testing'] = True
  client = current_app().test_client()
  return client

class TestApp():

  def test_home_page(self, client):
    response = client.get('/')
    assert response.status_code == 200