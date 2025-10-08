import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    usuario = "root"          
    senha = "nova_senha"       
    host = "localhost"        
    banco = "userdb"         
    porta = 3306              

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
