from app.posts.routes import post

class TestPost(object):

  def test_post_new_route_exits(self, client):
    response = client.get('/new')
    assert response.status_code == 200
  
  def test_post_new_contains_a_message(self, client):
    response = client.get('/new')
    assert b'What is on your mind' in response.data