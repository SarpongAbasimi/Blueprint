from flask import Flask
from app.main.routes import main
from app.posts.routes import post

def current_app():
  app = Flask(__name__)

  app.register_blueprint(main)
  app.register_blueprint(post)
  return app