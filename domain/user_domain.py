class UserDomain:
    def __init__(self, email, senha, id =None):
        self.id = id
        self.email = email
        self.senha = senha


    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "senha": self.senha
        }

