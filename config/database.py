import os
import urllib.parse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

def init_db(app):
    """
    Inicializa o banco de dados Supabase via SQLAlchemy com SSL.
    """
    # Variáveis de ambiente ou valores padrão
    usuario = os.getenv("DB_USER", "postgres")
    senha = os.getenv("DB_PASS", "marMAR@02")  # senha com @
    host = os.getenv("DB_HOST", "db.iuxpgppxturbydloixyq.supabase.co")
    porta = os.getenv("DB_PORT", "5432")  
    banco = os.getenv("DB_NAME", "postgres")

    # Escapa caracteres especiais
    usuario = urllib.parse.quote_plus(usuario)
    senha = urllib.parse.quote_plus(senha)

    # Monta string de conexão
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
            print("✅ Conexão com o banco bem-sucedida! Resultado teste:", result.scalar())
    except Exception as e:
        print("❌ Erro ao conectar no banco:", e)
        raise
