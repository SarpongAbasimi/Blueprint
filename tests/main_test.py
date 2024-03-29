import pytest

@pytest.fixture()
def response(client):
  response = client.get('/')
  return response

class TestMainRoutes():

  def test_index_page(self, response):
    assert response.status_code == 200
  
  def test_index_content_type(self, response):
    assert response.content_type == 'text/html; charset=utf-8'

  @pytest.mark.skip(reason='I took this from the home page for now')
  def test_index_page_content(self, response):
    assert b'Welcome To The Home Page' in response.data
  
  def test_to_see_create_new_post_on_page(self, response):
    assert b'create post' in response.data