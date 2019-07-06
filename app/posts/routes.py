from flask import Blueprint

post = Blueprint('post', __name__)

@post.route('/new', methods=['GET'])
def new():
  return 'What is on your mind'



