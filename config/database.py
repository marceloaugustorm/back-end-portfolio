import os
import urllib.parse
import socket
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

def init_db(app):
    """
    Inicializa o banco de dados Supabase via SQLAlchemy com SSL, forçando IPv4.
    """
    usuario = os.getenv("DB_USER", "postgres")
    senha = os.getenv("DB_PASS", "marMAR@02")
    host = os.getenv("DB_HOST", "db.iuxpgppxturbydloixyq.supabase.co")
    porta = os.getenv("DB_PORT", "5432")
    banco = os.getenv("DB_NAME", "postgres")

    # Escapa caracteres especiais
    usuario = urllib.parse.quote_plus(usuario)
    senha = urllib.parse.quote_plus(senha)

    # Resolve host para IPv4
    try:
        ipv4 = socket.gethostbyname(host)
        print(f"🌐 Resolvendo {host} para IPv4: {ipv4}")
    except Exception as e:
        print("❌ Erro ao resolver host para IPv4:", e)
        raise

    # Monta string de conexão usando IPv4
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql+psycopg2://{usuario}:{senha}@{ipv4}:{porta}/{banco}?sslmode=require"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Teste de conexão
    try:
        with app.app_context():
            result = db.session.execute(text("SELECT 1;"))
            print("✅ Conexão com o banco bem-sucedida! Resultado teste:", result.scalar())
    except Exception as e:
        print("❌ Erro ao conectar no banco:", e)
        raise
