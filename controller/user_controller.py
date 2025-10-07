from flask import request, jsonify
from service.user_service import UserService
from flask_jwt_extended import create_access_token


user_service = UserService()

def init_routes(app):
    @app.route("/cadastra", methods=["POST"])
    def criar_usuario():
        data = request.get_json()
        email = data.get("email")
        senha = data.get("senha")
        resultado = user_service.create_user(email, senha)
        return jsonify(resultado)

    @app.route("/login", methods=["POST"])
    def logar_usuario():
        data = request.get_json()
        email = data.get("email")
        senha = data.get("senha")
        user = user_service.logar_user(email, senha)

        if user:
            access_token = create_access_token(identity=user.id)
            return jsonify({
                "message": "Usuário logado com sucesso",
                "access_token": access_token
            })
        else:
            return jsonify({"message": "Falha ao fazer login"}), 401

