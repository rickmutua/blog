from flask import render_template, redirect, request, url_for, abort
from flask_login import login_required, current_user

from . import main
from ..admin import admin
from .forms import ReviewForm, BlogForm, EditBlog, DeleteBlog, DeleteComment
from ..models import Blog, Review, User
from .. import db


@main.route('/')
@login_required

def index():

    blogs = Blog.get_blog(id)

    return render_template('index.html', blogs=blogs)


@admin.route('/dashboard')
@login_required

def check_user():

    if current_user.id != 1:
        abort(403)

    return render_template('admin/dashboard.html')


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


@admin.route('/blog/new', methods=['GET', 'POST'])
def new_blog():

    form = BlogForm()

    if form.validate_on_submit():

        title = form.title.data

        description = form.description.data

        blog = form.blog.data

        new_blog = Blog(blog=blog, title=title, description=description)

        new_blog.save_blog()

        return redirect(url_for('.index'))

    return render_template('new_blog.html', blog_form=form)


@main.route('/blog/review/new/<int:id>', methods=['GET', 'POST'])
def new_review(id):

    blog = Blog.query.filter_by(id=id).first()

    if blog is None:
        abort(404)

    form = ReviewForm()

    if form.validate_on_submit():

        review = form.review.data

        new_review = Review(review=review, user=current_user)

        new_review.save_review()

        return redirect(url_for('.single_blog', id=blog.id))

    return render_template('blog.html', review_form=form, blog=blog)


@admin.route('delete/blog/<int:id>', methods=['GET', 'POST'])
def delete_blog(id):

    blog = Blog.delete_blog(id)

    return redirect(url_for('.index'))


@admin.route('delete/review/<int:id>', methods=['GET', 'POST'])
def delete_review(id):

    review = Review.delete_blog(id)

    return redirect(url_for('.single_blog'))


@admin.route('edit/blog/<int:id>', methods=['GET', 'POST'])
def edit_blog(id):

    edit = Review.delete_blog(id)

    return redirect(url_for('.single_blog'))

