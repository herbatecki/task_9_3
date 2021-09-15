from typing import Sized
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms import validators
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField('title' , validators=[DataRequired()])
    description = TextAreaField('description',validators=[DataRequired()])
    done = BooleanField('done')