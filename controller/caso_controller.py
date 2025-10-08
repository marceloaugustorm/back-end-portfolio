from flask import request, jsonify
from service.caso_service import CasoService
import base64

caso_service = CasoService()

def init_routes(app):
    @app.route("/caso", methods=["POST"])
    def create_case():
        nome = request.form.get("nome")
        raca = request.form.get("raca")
        idade = request.form.get("idade")
        descricao = request.form.get("descricao")
        fotos_files = request.files.getlist("foto")

        foto_base64 = None
        if fotos_files and fotos_files[0].filename:
            ext = fotos_files[0].filename.split('.')[-1]
            foto_base64 = f"data:image/{ext};base64,{base64.b64encode(fotos_files[0].read()).decode('utf-8')}"

        novo_caso = caso_service.criar_caso(
            nome=nome,
            raca=raca,
            idade=idade,
            descricao=descricao,
            foto=foto_base64
        )

        return jsonify({
            "mensagem": novo_caso["mensagem"],
            "id": novo_caso["id"],
            "foto": foto_base64
        }), 201

    @app.route("/caso", methods=["GET"])
    def get_casos():
        casos = caso_service.get_casos()
        return jsonify(casos), 200

    @app.route("/caso/<int:id>", methods=["DELETE"])
    def delete_caso(id):
        resultado = caso_service.excluir_casos(id)
        if resultado is None:
            return jsonify({"mensagem": "Caso não encontrado"}), 404
        return jsonify({"mensagem": "Caso excluído com sucesso", "id": id}), 200

    @app.route("/caso/<int:id>", methods=["PUT"])
    def put_case(id):
        nome = request.form.get("nome")
        raca = request.form.get("raca")
        idade = request.form.get("idade")
        descricao = request.form.get("descricao")
        foto_file = request.files.get("foto")  # apenas 1 foto

        foto_base64 = None
        if foto_file and foto_file.filename:
            ext = foto_file.filename.split('.')[-1]
            foto_base64 = f"data:image/{ext};base64,{base64.b64encode(foto_file.read()).decode('utf-8')}"

        resultado = caso_service.update_caso(
            id=id,
            nome=nome,
            raca=raca,
            idade=idade,
            descricao=descricao,
            foto=foto_base64
        )

        if not resultado:
            return jsonify({"mensagem": "Caso não encontrado"}), 404

        return jsonify(resultado), 200
