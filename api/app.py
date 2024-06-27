import os

from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from db import db

from schedule.blueprints import EpisodesBlueprint, ShowsBlueprint
from auth.blueprints import UsersBlueprint



def create_app(db_url=None):
  app = Flask(__name__)
  app.config["PROPAGATE_EXCEPTIONS"] = True
  app.config["API_TITLE"] = "Silver Box Radio"
  app.config["API_VERSION"] = "v1"
  app.config["OPENAPI_VERSION"] = "3.0.3"
  app.config["OPENAPI_URL_PREFIX"] = "/"
  app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
  app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
  app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///sqlite.db")
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  app.config["JWT_SECRET_KEY"] = "TEMPORARY"
  db.init_app(app)
  api = Api(app)
  jwt = JWTManager(app)

  with app.app_context():
    import schedule.models
    import auth.models
    db.create_all()

  api.register_blueprint(ShowsBlueprint)
  api.register_blueprint(EpisodesBlueprint)
  api.register_blueprint(UsersBlueprint)
  
  return app
