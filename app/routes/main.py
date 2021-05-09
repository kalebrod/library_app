from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_required,current_user
from werkzeug.security import check_password_hash

from app.extensions import db
from app.models import User

main = Blueprint('main', __name__)

@main.route('/index')
@login_required
def index():
    return render_template('main/index.html',user=current_user)