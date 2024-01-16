
import os
import secrets
from flask import Flask, request
from flask_smorest import Api
from flask_jwt_extended import jwt_manager


from db import db
import models

from resources.items import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.user import blp as UserBlueprint


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"]="Stores Rest API"
    app.config["API_VERSION"]="V1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"]="/"
    app.config["OPENAPI_SWAGGER_UI_PATH"]="/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "hptts://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "postgresql://username:password@localhost:5432/dbname")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "mody"
    db.init_app(app)
    api = Api(app)
    # app.config["JWT_SECRET_KEY"] = "mody"  #98234392759459394844318359179656412331 #secrets.SystemRandom().getrandbits(128) run this code in tirmnal after type python  then cope the code number 
    
    jwt = jwt_manager(app)
    
    @app.before_first_request
    def create_tables():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(UserBlueprint)
    
    
    return app


    #  