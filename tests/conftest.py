import pytest
from app import create_app, db

@pytest.fixture()
def client():
  test_env = create_app('testing')

  test_env.app_context().push()
  db.create_all()

  client = test_env.test_client()

  yield client

  db.drop_all()