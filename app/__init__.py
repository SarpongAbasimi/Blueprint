import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from app.config import configs

db = SQLAlchemy()
boostrap = Bootstrap()

def create_app(config_name='development'):
  app = Flask(__name__)
  app.config.from_object(configs.get(config_name))
  
  db.init_app(app)
  boostrap.init_app(app)

  from app.main.routes import main
  from app.posts.routes import post

  app.register_blueprint(main)
  app.register_blueprint(post)
  
  return app