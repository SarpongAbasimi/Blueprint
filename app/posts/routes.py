from flask import Blueprint, render_template

post = Blueprint('post', __name__)

@post.route('/new', methods=['GET'])
def new():
  return render_template('new.html')



