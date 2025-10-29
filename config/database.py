import os
import urllib.parse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

def init_db(app):
    """
    Inicializa o banco interno da Render via SQLAlchemy com SSL.
    """
    usuario = os.getenv("DB_USER")
    senha = os.getenv("DB_PASS")
    host = os.getenv("DB_HOST")
    porta = os.getenv("DB_PORT")
    banco = os.getenv("DB_NAME")

    # Escapa caracteres especiais
    usuario = urllib.parse.quote_plus(usuario)
    senha = urllib.parse.quote_plus(senha)

    # String de conexão
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}?sslmode=require"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa SQLAlchemy
    db.init_app(app)

    # Teste de conexão
    try:
        with app.app_context():
            result = db.session.execute(text("SELECT 1;"))
            print("✅ Conexão com o banco Render bem-sucedida! Resultado:", result.scalar())
    except Exception as e:
        print("❌ Erro ao conectar no banco:", e)
        raise
