import os
from flask import Flask, send_from_directory
from flask_jwt_extended import JWTManager
from config.database import init_db, db
from controller.user_controller import init_routes as user_routes
from controller.caso_controller import init_routes as caso_routes
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_folder="build/static", template_folder="build")
    CORS(app)
    
    app.config["JWT_SECRET_KEY"] = "flaroque"  
    JWTManager(app)

    # Inicializa banco
    init_db(app)

    # Registra rotas
    user_routes(app)
    caso_routes(app)

    with app.app_context():
        db.create_all()
        print("Tabelas criadas!")

    # Serve React build
    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def serve(path):
        if path != "" and os.path.exists(f"build/{path}"):
            return send_from_directory("build", path)
        else:
            return send_from_directory("build", "index.html")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
