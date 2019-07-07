import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  DEBUG = os.getenv('DEBUG_STATE')
  SECRET_KEY = os.getenv('SECRET_KEY') or 'notsosecret'

class Development(Config):
  DEBUG = True
  DATABASE_URI = os.getenv('DEVELOPMENT_DATABASE_URI')

class Testing(Config):
  TESTING = True
  TEST_DB = os.getenv('TEST_DATABASE_URI')

  