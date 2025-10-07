import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    raiz_dir = os.path.abspath(os.path.dirname(__file__))  # pasta config
    db_path = os.path.join(raiz_dir, "../user.db")          # caminho relativo para raiz
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
