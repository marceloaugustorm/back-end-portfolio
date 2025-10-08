from domain.caso_domain import CasoDomain
from model.caso import Caso
from config.database import db
import json
import cloudinary
import cloudinary.uploader
import os


cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

class CasoService:
    def criar_caso(self, nome, raca, idade, descricao, fotos):
        urls = []

        for img in fotos:
            if img and img.filename != "":
                result = cloudinary.uploader.upload(img)
                urls.append(result["secure_url"])

        imagens_como_string = json.dumps(urls)

        caso = Caso(
            nome=nome,
            raca=raca,
            idade=idade,
            descricao=descricao,
            foto=imagens_como_string
        )

        db.session.add(caso)
        db.session.commit()

        return {"mensagem": "Caso criado com sucesso", "id": caso.id}

    def get_casos(self):
        casos = Caso.query.all()
        lista = []
        for c in casos:
            lista.append({
                "id": c.id,
                "nome": c.nome,
                "raca": c.raca,
                "idade": c.idade,
                "descricao": c.descricao,
                "foto": json.loads(c.foto) if c.foto else []
            })
        return lista

    def excluir_casos(self, id):
        caso = Caso.query.get(id)
        if not caso:
            return None
        db.session.delete(caso)
        db.session.commit()
        return {"id": id}

    def update_caso(self, id, nome, raca, idade, descricao, fotos):
        caso = Caso.query.get(id)
        if not caso:
            return None

        caso.nome = nome
        caso.raca = raca
        caso.idade = idade
        caso.descricao = descricao

        # Se enviar nova foto, faz upload e substitui
        if fotos:
            urls = []
            for img in fotos:
                if img and img.filename != "":
                    result = cloudinary.uploader.upload(img)
                    urls.append(result["secure_url"])
            if urls:
                caso.foto = json.dumps(urls)  # substitui fotos antigas

        db.session.commit()

        return {
            "id": caso.id,
            "nome": caso.nome,
            "raca": caso.raca,
            "idade": caso.idade,
            "descricao": caso.descricao,
            "foto": json.loads(caso.foto) if caso.foto else []
        }
