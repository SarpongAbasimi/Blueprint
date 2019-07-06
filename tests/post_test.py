import pytest
from app.posts.routes import post

@pytest.fixture(autouse=True)
def response(client):
  response = client.get('/new')
  return response

class TestPost(object):

  def test_post_new_route_exits(self, response):
    assert response.status_code == 200
  
  def test_post_new_contains_a_message(self, response):
    assert b'What is on your mind' in response.data