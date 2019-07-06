
class TestMainRoutes():

  def test_home_page(self, client):
    response = client.get('/')
    assert response.status_code == 200

  def test_home_page_content(self, client):
    response = client.get('/')
    assert b'This is the home page' in response.data



  