import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  DEBUG = os.getenv('DEBUG_STATE')
  SECRET_KEY = os.getenv('SECRET_KEY') or 'notsosecret'

class Development(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOPMENT_DATABASE_URI') or 'sqlite:///database/dev.db'

class Testing(Config):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI') or 'sqlite:///database/test.db'


configs = {
  'development': Development,
  'testing': Testing
}