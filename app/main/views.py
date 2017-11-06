from flask import render_template
from flask_login import login_required

from . import main
from ..models import Blog

@main.route('/')
@login_required

def index():

    blogs = Blog.get_blog(id)

    return render_template('index.html', blogs=blogs)