from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class BlogForm(FlaskForm):

    title = StringField('Blog Title', validators=[Required()])

    description = TextAreaField('Blog Description', validators=[Required()])

    blog = SubmitField('Submit')