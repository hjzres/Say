from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user

auth = Blueprint('auth', __name__)

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 3:
            # Email should be 3 characters or more!
            pass
        elif len(username) < 4:
            # username should be 4 characters or more!
            pass
        elif password1 != password2:
            # Passwords do not match!
            pass
        elif len(password1) <= 6:
            # Password should be at least 6 characters
            pass
        else:
            hashed_password = generate_password_hash(password1, method='pbkdf2:sha256')

            new_user = User(email=email, username=username, password=hashed_password)

            db.session.add(new_user)
            db.session.commit()
        
    return render_template("sign_up.html")

@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('views.home'))
        else:
            # Incorrect email or password!
            pass

    return render_template("login.html")