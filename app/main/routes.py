from flask import Blueprint, render_template
from app.models import Todo

main = Blueprint('main', __name__)

@main.route('/')
def index():
  todos = Todo.query.order_by(Todo.id.desc()).all()
  return render_template('index.html', todos=todos)