import pytest
from app import create_app, db
from app.models import Todo

@pytest.fixture()
def client():
  """ set the app to use testing environemnt """
  test_env = create_app('testing')

  test_env.app_context().push()
  db.create_all()

  client = test_env.test_client()

  yield client

  db.drop_all()