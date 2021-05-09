from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from app.extensions import db
from app.models import User

auth = Blueprint('auth', __name__)

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        unhashed = request.form['password']

        user = User(
            username = username,
            upassword = unhashed
        )

        db.session.add(user)
        db.session.commit()
    
        return redirect(url_for('auth.login'))
    
    return render_template('auth/signup.html')

@auth.route('/')
@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash('User or password incorrect')
            return redirect(request.url)

        login_user(user)
        return redirect(url_for('main.index'))
    
    return render_template('auth/login.html')

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))