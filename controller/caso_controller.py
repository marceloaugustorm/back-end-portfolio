from flask import request, jsonify, send_from_directory
from service.caso_service import CasoService
import os

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

caso_service = CasoService()

def init_routes(app):
    @app.route("/caso", methods=["POST"])
    def create_case():
        data = request.form if request.form else request.get_json()
        nome = data.get("nome")
        raca = data.get("raca")
        idade = data.get("idade")
        descricao = data.get("descricao")
        foto = request.files.getlist("foto")
        caminhos_imagens = []

        for img in foto:
            if img.filename != "":
                caminho = os.path.join(UPLOAD_FOLDER, img.filename)
                img.save(caminho)
                caminhos_imagens.append(img.filename)

        novo_caso = caso_service.criar_caso(
            nome=nome,
            raca=raca,
            idade=idade,
            descricao=descricao,
            foto=caminhos_imagens
        )

        return jsonify({"mensagem": "Caso criado com sucesso!", "caso": novo_caso}), 201

    @app.route("/caso", methods=["GET"])
    def get_casos():
        casos = caso_service.get_casos()
        return jsonify(casos), 200

    @app.route("/uploads/<filename>")
    def uploaded_file(filename):
        caminho_completo = os.path.join(UPLOAD_FOLDER, filename)
        print(f"🖼️ Servindo imagem: {caminho_completo}")  

        if not os.path.exists(caminho_completo):
            return jsonify({"erro": "Arquivo não encontrado"}), 404

        return send_from_directory(UPLOAD_FOLDER, filename)
    

    @app.route("/caso/<int:id>", methods=["DELETE"])
    def delete_caso(id):
        resultado = caso_service.excluir_casos(id)

        if resultado is None:
            return jsonify({"mensagem": "Caso não encontrado"}), 404
        else:
            return jsonify({"mensagem": "Caso excluído com sucesso", "id": id}), 200
        

    @app.route("/caso/<int:id>", methods=["PUT"])
    def put_case(id):
       
        nome = request.form.get("nome")
        raca = request.form.get("raca")
        idade = request.form.get("idade")
        descricao = request.form.get("descricao")
        fotos = request.files.getlist("foto")

        caminhos_imagens = []
        for img in fotos:
            if img.filename != "":
                caminho = os.path.join(UPLOAD_FOLDER, img.filename)
                img.save(caminho)
                caminhos_imagens.append(img.filename)

        
        resultado = caso_service.update_caso(
            id=id,
            nome=nome,
            raca=raca,
            idade=idade,
            descricao=descricao,
            foto=caminhos_imagens if caminhos_imagens else None
        )

        if not resultado:
            return jsonify({"mensagem": "Caso não encontrado"}), 404

        return jsonify(resultado), 200
