from flask import render_template, redirect, request, url_for, abort
from flask_login import login_required, current_user

from ..models import User
from .forms import BlogForm, ReviewForm
from . import admin

from .. import db
