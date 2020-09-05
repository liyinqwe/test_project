from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import TestConfig, STATIC_FOLDER, TEMPLATES_FOLDER

app = Flask(
    __name__,
    template_folder=TEMPLATES_FOLDER,
    static_folder=STATIC_FOLDER,
    static_url_path=""

)

app.config.from_object(TestConfig)

db = SQLAlchemy(app)

CORS(app)

image_code_dict = {

}


@app.route("/")
def index():
    return app.send_static_file("login.html")


def create_app():
    from backend.verification.views import verification_bp
    app.register_blueprint(verification_bp, url_prefix="/verifications")

    from backend.user.views import users_bp
    app.register_blueprint(users_bp, url_prefix="/users")

    return app
