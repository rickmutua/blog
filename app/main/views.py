from flask import render_template, redirect, request, url_for, abort
from flask_login import login_required, current_user

from . import main
from ..models import Blog, Review, User


@main.route('/')
@login_required

def index():

    blogs = Blog.get_blog(id)

    return render_template('index.html', blogs=blogs)


@main.route('/blog/<int:id>')
def single_blog(id):

    single_blog = Blog.query.get(id)

    reviews = Review.get_reviews(id)

    if single_blog is None:
        abort (404)

    return render_template('blog.html', blog=single_blog, reviews=reviews)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)