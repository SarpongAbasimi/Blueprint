import pytest
from app.posts.routes import post

@pytest.fixture()
def response(client):
  response = client.get('/new')
  return response

class TestPost(object):


  def test_post_new_route_exits(self, response):
    assert response.status_code == 200


  def test_post_new_contains_a_message(self, response):
    assert b'What is on your mind?' in response.data
    
  @pytest.mark.skip()
  def test_post_new_allow_user_to_post_toDo_(self, client):
    post_message = client.post('/create', data=('I need to go shopping'),follow_redirects=True)
    assert b'Welcome To The Home Page' in  post_message.data

  @pytest.mark.skip(reason='I need a better understanding of how to set up a config file')
  def test_post_is_stored_shown_on_index_page(self, client):
    post_message = client.post('/create', data=('I need to go shopping'),follow_redirects=True)
    assert b'I need to go shopping' in post_message.data
  
  
