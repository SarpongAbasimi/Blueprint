import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.main.routes import main
from app.posts.routes import post
from app.config import configs

def current_app(config_name=configs.get('development')):
  app = Flask(__name__)
  app.config.from_object(config_name)

  app.register_blueprint(main)
  app.register_blueprint(post)
  return app