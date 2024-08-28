import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import sqlite3

load_dotenv()

db = SQLAlchemy()

def init_db():
    with open('schema.sql', 'r') as f:
        schema = f.read()
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()
    

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("MY_SECRET_KEY")

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

    db.init_app(app)

    init_db()

    from .views import views
    from .auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app