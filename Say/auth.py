from flask import Blueprint, render_template, request, flash
from . import db
from .models import User
from werkzeug.security import generate_password_hash

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

@auth.route('/login')
def login():
    return render_template("login.html")