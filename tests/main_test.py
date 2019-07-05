import pytest
from app import current_app

@pytest.fixture()
def client():
  current_app().config['Testing'] = True
  client = current_app().test_client()
  return client

class TestMainRoutes():

  def test_home_page(self, client):
    response = client.get('/')
    assert response.status_code == 200
  
  def test_home_page_content(self, client):
    response = client.get('/')
    assert b'This is the home page' in response.data



  