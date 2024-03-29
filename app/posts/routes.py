from flask import Blueprint, render_template, redirect, url_for, request
from .forms import PostForm
from app import db
from app.models import Todo

post = Blueprint('post', __name__)

@post.route('/new', methods=['GET'])
def new():
  post_form = PostForm()
  return render_template('new.html', post_form = post_form)

@post.route('/create', methods=['POST'])
def create():
  post_form = PostForm()
  if request.method == 'POST' and post_form.validate_on_submit():
    to_do = Todo(content = post_form.todo.data)
    db.session.add(to_do)
    db.session.commit()
    return redirect(url_for('main.index'))

@post.route('/<int:id>')
def show(id):
  data = Todo.query.filter_by(id=id).first()
  return render_template('show.html', data=data)

@post.route('/<int:id>/edit')
def edit(id):
  edit_form = PostForm()
  get_todo_data = Todo.query.filter_by(id=id).first()
  edit_form.todo.data = get_todo_data.content
  return render_template('edit.html', edit_form=edit_form, id=id)

@post.route('/<int:id>', methods=['POST'])
def update(id):
  form = PostForm()
  new_update = Todo.query.filter_by(id=id).first()
  new_update.content = form.todo.data 
  db.session.commit()
  return redirect(url_for('main.index'))

@post.route('/delete/<int:id>')
def destroy(id):
  delete_todo = Todo.query.filter_by(id=id).first()
  db.session.delete(delete_todo)
  db.session.commit()
  return redirect(url_for('main.index'))


