import os

from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from auth.models import UserModel
from db import db

from schedule.blueprints import EpisodesBlueprint, ShowsBlueprint
from auth.blueprints import UsersBlueprint, InvitesBlueprint



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
  
  @jwt.expired_token_loader
  def expired_token_callback(jwt_header, jwt_payload):
    return (jsonify({
      "message": "The token has expired.",
      "error": "token_expired"
    }), 401)
    
  @jwt.invalid_token_loader
  def invalid_token_callback(error):
    return (jsonify({
      "message": "Signature verification failed.",
      "error": "invalid_token"
      }), 401)
    
  @jwt.unauthorized_loader
  def missing_token_callback(error):
    return (jsonify({
      "message": "Request does not contain an access token.",
      "error": "authorization_required"
    }), 401)
  
  @jwt.additional_claims_loader
  def add_claims_to_jwt(identity):
    user = db.session.get(UserModel, identity)
    if user and user.is_admin:
      return { "is_admin": True }
    return { "is_admin": False }

  with app.app_context():
    import schedule.models
    import auth.models
    db.create_all()

  api.register_blueprint(ShowsBlueprint)
  api.register_blueprint(EpisodesBlueprint)
  api.register_blueprint(UsersBlueprint)
  api.register_blueprint(InvitesBlueprint)
  
  return app
