import pytest
from app.posts.routes import post


class TestPost(object):
  def test_post_new_route_exits(self, client):
    response = client.get('/new')
    assert response.status_code == 200

  def test_post_new_contains_a_message(self, client):
    response = client.get('/new')
    assert b'Back to home' in response.data
    
  def test_post_new_allow_user_to_post_toDo_(self, client):
    post_message = client.post('/create',
    data = dict(todo='go to sch'),
    follow_redirects=True)
    assert b'go to sch' in  post_message.data
  
  @pytest.mark.parametrize('todolist', [{'todo': 'I need to go shopping'}])
  def test_post_is_stored_shown_on_index_page(self, client, todolist):
    post_message = client.post('/create', 
    data=todolist,
    follow_redirects=True)
    assert b'I need to go shopping' in post_message.data

  @pytest.mark.parametrize('todolist', [{'todo': 'I need to buy some food'}])
  def test_shows_post_when_passed_an_id(self, client, todolist):
    post_message = client.post('/create', 
    data=todolist,
    follow_redirects=True)
    
    response = client.get('/1')
    assert b'I need to buy some food' in response.data
    assert b'edit' in response.data

  def test_shows_post_when_passed_id(self, client):
    response = client.get('/1')
    assert b'Sorry, the post was not found' in response.data
    assert b'Back to home' in response.data

  @pytest.mark.parametrize('new_todo', [{'todo': 'Make my test pass'}])
  def test_edit_page(self, client, new_todo):
    create_post = client.post('/create',
    data = new_todo,
    follow_redirects = True)
    response = client.get('/1/edit')
    assert b'cancel' in response.data

  @pytest.mark.parametrize('new_todo', [{'todo': 'I need to sing a song'}])
  def test_post_can_be_updated(self, client, new_todo):
    response = client.post('/create',
    data= new_todo,
    follow_redirects=True)

    updatate_post = client.post('/1',
    data=dict(todo='I need to make a food app'),
    follow_redirects=True)
    
    assert updatate_post.status_code == 200
    assert b'I need to make a food app' in updatate_post.data
  
  def test_post_can_be_deleted(self, client):
    post_message = client.post('/create',
    data=dict(todo='I need to purchase pizza'),
    follow_redirects= True)
    response = client.get('/delete/1')
    assert b'I need to purchase pizza' not in response.data
