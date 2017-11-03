from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

from . import db


class Blog(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)

    title = db.Column(db.String(100))

    description = db.Column(db.String(200))

    blog = db.Column(db.String)

    posted = db.Column(db.DateTime, default=datetime.now(tz=None))


class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)

    review = db.Column(db.String)

    posted = db.Column(db.DateTime, default=datetime.now(tz=None))


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key= True)

    username = db.Column(db.String(25))

    email = db.Column(db.String(50))

    password_hash = db.Column(db.String(25))



