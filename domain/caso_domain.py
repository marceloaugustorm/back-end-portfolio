class CasoDomain:
    def __init__(self, nome, raca, idade, descricao, foto):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.descricao = descricao
        self.foto = foto

    
    def to_dict_caso(self):
        return{
            "nome": self.nome,
            "raca": self.raca,
            "idade": self. idade,
            "descricao": self.descricao,
            "foto": self.foto
        }