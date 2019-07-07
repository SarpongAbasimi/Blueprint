from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
  todo = StringField('toDos', validators=[DataRequired()])
  submit = SubmitField('submit')