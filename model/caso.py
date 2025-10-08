from config.database import db
import json

class Caso(db.Model):  
    __tablename__ = 'casos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    raca = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)  
    foto = db.Column(db.Text, nullable=True)  

    def to_dict_caso(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "raca": self.raca,
            "idade": self.idade,
            "descricao": self.descricao,
            "foto": self.foto  
        }
