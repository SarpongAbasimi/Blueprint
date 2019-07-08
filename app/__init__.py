import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import configs

db = SQLAlchemy()

def create_app(config_name='development'):
  app = Flask(__name__)
  app.config.from_object(configs.get(config_name))
  db.init_app(app)

  with app.app_context():
    db.create_all()

  from app.main.routes import main
  from app.posts.routes import post

  app.register_blueprint(main)
  app.register_blueprint(post)
  return app

