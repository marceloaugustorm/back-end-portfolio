from model.user import User
from domain.user_domain import UserDomain
from config.database import db

class UserService:
    def create_user(self,email, senha):
       
       new_user = UserDomain(email, senha)

       user = User(
           email = new_user.email,
           senha = new_user.senha
       )

       

       db.session.add(user)
       db.session.commit()
       return {"message": "Usuário criado com sucesso", "id": user.id}


    def logar_user(self, email, senha):
        user = User.query.filter_by(email=email, senha=senha).first()
        return user
        

       
   

