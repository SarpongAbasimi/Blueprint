import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.main.routes import main
from app.posts.routes import post
from app.config import configs

db = SQLAlchemy()

def current_app(config_name='development'):
  app = Flask(__name__)
  app.config.from_object(configs.get(config_name))
  db.init_app(app)

  app.register_blueprint(main)
  app.register_blueprint(post)
  return app