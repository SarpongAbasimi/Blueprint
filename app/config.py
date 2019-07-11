import os
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, '.env'))

class Config:
  DEBUG = os.getenv('DEBUG_STATE')
  SECRET_KEY = os.getenv('SECRET_KEY') or 'notsosecret'

class Development(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOPMENT_DATABASE_URI') or 'sqlite:///database/clidev.db'

class Testing(Config):
  TESTING = True
  WTF_CSRF_ENABLED = False
  SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI') or 'sqlite:///database/clitest.db'

configs = {
  'development': Development,
  'testing': Testing
}