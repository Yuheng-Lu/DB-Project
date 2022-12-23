import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from blocklist import BLOCKLIST
from db import db
from resources.customer import blp as CustomerBlueprint
from resources.insurance import blp as InsuranceBlueprint
from resources.employee import blp as EmployeeBlueprint
from resources.user import blp as UserBlueprint
from resources.machine_learning import blp as MLBlueprint
from resources.home import blp as HomeBlueprint


def create_app(db_url=None):
    app = Flask(__name__)
    load_dotenv()
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    # !!! This is a really bad idea to put DB link at here where everybody can access it!!!#
    # Due to timing limitation, I directly put it here, as there should not be any sensitive data included#
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://mvgevlla:3a9x7YgMIazdwyzaHCdimujNKRMGnYQX@mahmud.db.elephantsql.com/mvgevlla"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "this should be a better secret"
    jwt = JWTManager(app)

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.",
                    "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.",
                    "error": "token_revoked"}
            ),
            401,
        )

    with app.app_context():
        db.create_all()
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(CustomerBlueprint)
    api.register_blueprint(InsuranceBlueprint)
    api.register_blueprint(EmployeeBlueprint)
    api.register_blueprint(MLBlueprint)
    api.register_blueprint(HomeBlueprint)

    return app
