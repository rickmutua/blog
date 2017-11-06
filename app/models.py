from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager

from . import db


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


class Blog(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)

    title = db.Column(db.String(200))

    description = db.Column(db.String(300))

    blog = db.Column(db.String)

    posted = db.Column(db.DateTime, default=datetime.now(tz=None))

    review_id = db.relationship('Review', backref='blog', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_blog(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_blog(cls, id):
        blog = Blog.query.filter_by(blog_id=id).all()
        return blog


class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)

    review = db.Column(db.String)

    posted = db.Column(db.DateTime, default=datetime.now(tz=None))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls, id):
        reviews = Review.query.filter_by(blog_id=id).all()
        return reviews


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), index = True)
    email = db.Column(db.String(250), unique=True, index=True)

    password_hash = db.Column(db.String(400))

    blog_id = db.relationship('Blog', backref='user', lazy='dynamic')
    review_id = db.relationship('Review', backref='user', lazy='dynamic')
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('Access to the password attribute Denied!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)

    role = db.Column(db.String)

    user = db.relationship('User', backref='role', lazy='dynamic')


    def __repr__(self):
        return f'User {self.name}'




