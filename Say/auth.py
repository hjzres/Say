from flask import Blueprint, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/sign-up')
def sign_up():
    return '<h1>Sign up</h1>'

@auth.route('/login')
def login():
    return '<h1>Login</h1>'