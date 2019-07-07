import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.main.routes import main
from app.posts.routes import post

def current_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'mykey'


  app.register_blueprint(main)
  app.register_blueprint(post)
  return app