from flask import request, jsonify
from service.caso_service import CasoService

caso_service = CasoService()

def init_routes(app):
    @app.route("/caso", methods=["POST"])
    def create_case():
        nome = request.form.get("nome")
        raca = request.form.get("raca")
        idade = request.form.get("idade")
        descricao = request.form.get("descricao")
        fotos = request.files.getlist("foto")

        novo_caso = caso_service.criar_caso(
            nome=nome,
            raca=raca,
            idade=idade,
            descricao=descricao,
            fotos=fotos
        )
        return jsonify(novo_caso), 201

    @app.route("/caso", methods=["GET"])
    def get_casos():
        return jsonify(caso_service.get_casos()), 200

    @app.route("/caso/<int:id>", methods=["PUT"])
    def update_caso(id):
        nome = request.form.get("nome")
        raca = request.form.get("raca")
        idade = request.form.get("idade")
        descricao = request.form.get("descricao")

        # pega o arquivo único enviado
        foto = request.files.get("foto")
        fotos = [foto] if foto else []

        resultado = caso_service.update_caso(id, nome, raca, idade, descricao, fotos)
        if not resultado:
            return jsonify({"mensagem": "Caso não encontrado"}), 404
        return jsonify(resultado), 200

    @app.route("/caso/<int:id>", methods=["DELETE"])
    def delete_caso(id):
        resultado = caso_service.excluir_casos(id)
        if not resultado:
            return jsonify({"mensagem": "Caso não encontrado"}), 404
        return jsonify({"mensagem": "Caso excluído", "id": id}), 200
