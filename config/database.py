import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    # Pega as configurações do banco do ambiente, se disponíveis
    usuario = os.getenv("DB_USER", "root")
    senha = os.getenv("DB_PASS", "nova_senha")
    host = os.getenv("DB_HOST", "localhost")
    porta = int(os.getenv("DB_PORT", 3306))
    banco = os.getenv("DB_NAME", "userdb")

    # URI de conexão com PyMySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}"
    )

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
