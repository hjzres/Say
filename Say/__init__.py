import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import sqlite3

load_dotenv()

db = SQLAlchemy()

def init_db():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')
    print(f"Initializing database at {db_path}")
    with open('schema.sql', 'r') as f:
        schema = f.read()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()
    

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("MY_SECRET_KEY")

    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    print(f"SQLAlchemy is using the database at: {app.config['SQLALCHEMY_DATABASE_URI']}")

    db.init_app(app)

    init_db()

    from .views import views
    from .auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app