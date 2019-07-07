from flask import Blueprint, render_template, redirect, url_for
from .forms import PostForm

post = Blueprint('post', __name__)

@post.route('/new', methods=['GET'])
def new():
  post_form = PostForm()
  return render_template('new.html', post_form = post_form)

@post.route('/create', methods=['POST'])
def create():
  post_form = PostForm()
  return redirect(url_for('main.index'))





