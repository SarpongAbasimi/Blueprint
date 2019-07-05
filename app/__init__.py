from flask import Flask

def current_app():
  app = Flask(__name__)
  return app