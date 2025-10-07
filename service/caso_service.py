from domain.caso_domain import CasoDomain
from model.caso import Caso
from config.database import db
import json

class CasoService:
    def criar_caso(self, nome, raca, idade, descricao, foto):
    
        imagens_como_string = json.dumps(foto)
        new_caso = CasoDomain(nome, raca, idade, descricao, imagens_como_string)

       
        caso = Caso(
            nome=new_caso.nome,
            raca=new_caso.raca,
            idade=new_caso.idade,
            descricao=new_caso.descricao,
            foto=new_caso.foto 
        )

        db.session.add(caso)
        db.session.commit()

        return {"mensagem": "Caso criado com sucesso", "id": caso.id}

    def get_casos(self):
        casos = Caso.query.all()
        result = []

        for caso in casos:
            d = caso.to_dict_caso()
            try:
                d['foto'] = json.loads(d['foto'])
            except:
                d['foto'] = []
            result.append(d)

        return result
    

    def excluir_casos(self, id):
        caso = Caso.query.filter_by(id=id).first()

        if not caso:
            return None

        
        db.session.delete(caso)
        db.session.commit()

        return caso.to_dict_caso()


    def update_caso(self, id, nome, raca, idade, descricao, foto):
        new_caso = CasoDomain(nome, raca, idade, descricao, foto)

        caso = Caso.query.filter_by( id = id).first()

        if not caso:
            return None
        
        else:
            caso.nome = nome 
            caso.raca = raca
            caso.idade = idade
            caso.descricao =descricao
            
            if foto:
                caso.foto = foto

            db.session.commit()

            return {
            "id": caso.id,
            "nome": caso.nome,
            "raca": caso.raca,
            "idade": caso.idade,
            "descricao": caso.descricao,
            "foto": caso.foto,
        }

           




