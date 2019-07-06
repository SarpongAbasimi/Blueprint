import pytest

@pytest.fixture(autouse=True)
def response(client):
  response = client.get('/')
  return response

class TestMainRoutes():

  def test_index_page(self, response):
    assert response.status_code == 200
  
  def test_index_content_type(self, response):
    assert response.content_type == 'text/html; charset=utf-8'

  def test_index_page_content(self, response):
    assert b'Welcome To The Home Page' in response.data
  
  # @pytest.mark.parametrize('data', [('I need to go shopping'), ('I have to do my homework')])
  # def test_post_data_to_home_page(client, data):
  #   response = client.post('/', data, follow_redirects=True)
  #   print(response.data)




  