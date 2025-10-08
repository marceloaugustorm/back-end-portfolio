import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    usuario = os.getenv("DB_USER", "neondb_owner")
    senha = os.getenv("DB_PASS", "npg_xCUHpsn1z0lY")
    host = os.getenv("DB_HOST", "ep-cool-morning-ad79jm5x-pooler.c-2.us-east-1.aws.neon.tech")
    porta = int(os.getenv("DB_PORT", 5432))
    banco = os.getenv("DB_NAME", "neondb")

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}?sslmode=require"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
