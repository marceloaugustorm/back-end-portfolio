import os
import urllib.parse
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    """
    Inicializa o banco de dados Supabase via connection pooling (porta 6543),
    escapando caracteres especiais na senha/usuário e usando SSL.
    """
    # Variáveis de ambiente ou valores padrão
    usuario = os.getenv("DB_USER", "postgres.iuxpgppxturbydloixyq")  # usuário completo do Supabase
    senha = os.getenv("DB_PASS", "marMAR@02")  # senha com @
    host = os.getenv("DB_HOST", "aws-1-us-east-2.pooler.supabase.com")
    porta = os.getenv("DB_PORT", "6543")  # porta do PgBouncer (pooling)
    banco = os.getenv("DB_NAME", "postgres")

    # Escapa caracteres especiais
    usuario = urllib.parse.quote_plus(usuario)
    senha = urllib.parse.quote_plus(senha)

    # String de conexão válida para psycopg2
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}?sslmode=require"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa SQLAlchemy
    db.init_app(app)

    # Teste rápido de conexão
    try:
        with app.app_context():
            result = db.session.execute("SELECT 1;")
            print("Conexão com o banco bem-sucedida! Resultado teste:", result.scalar())
    except Exception as e:
        print("Erro ao conectar no banco:", e)
        raise
