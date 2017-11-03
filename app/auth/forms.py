from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField, ValidationError
from wtforms.validators import Required, EqualTo, Email

from ..models import User


class RegistrationForm(FlaskForm):

    email = StringField('Your Email Address', validators=[Required()])

    username = StringField('UserName', validators=[Required()])

    password = PasswordField('Password', validators=[Required(),
                                                     EqualTo('password_confirm', message='Password do no match!')])

    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('Email already exists')

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first()
            raise ValidationError('Username is taken')


class LoginForm(FlaskForm):

    email = StringField('Email Address', validators=[Required()])

    password = PasswordField('Password', validators=[Required()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Sign In')





