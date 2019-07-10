import pytest
from app.posts.routes import post

class TestPost(object):

  def test_post_new_route_exits(self, client):
    response = client.get('/new')
    assert response.status_code == 200

  def test_post_new_contains_a_message(self, client):
    response = client.get('/new')
    assert b'What is on your mind?' in response.data
    
  def test_post_new_allow_user_to_post_toDo_(self, client):
    post_message = client.post('/create',
    data = dict(todo='go to sch'),
    follow_redirects=True)
    print(post_message.data)
    assert b'go to sch' in  post_message.data

  @pytest.mark.skip(reason='I need a better understanding of how to set up a config file')
  def test_post_is_stored_shown_on_index_page(self, client):
    post_message = client.post('/create', data=('I need to go shopping'),follow_redirects=True)
    assert b'I need to go shopping' in post_message.data
  
  
