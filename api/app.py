from datetime import datetime, timedelta, timezone
from decouple import config
from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager, create_access_token, get_jwt, get_jwt_identity, set_access_cookies
from flask_cors import CORS

from auth.models import UserModel, TokenBlocklist
from db import db

from schedule.blueprints import EpisodesBlueprint, ShowsBlueprint
from auth.blueprints import UsersBlueprint, InvitesBlueprint

def create_app(db_url=None, cfg=config("CONFIG_OBJECT")):
  app = Flask(__name__)
  app.config.from_object(cfg)
  db.init_app(app)
  api = Api(app)
  jwt = JWTManager(app)
  cors = CORS(app, supports_credentials=True)
  
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
  
  @jwt.token_in_blocklist_loader
  def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
    return token is not None
  
  @jwt.revoked_token_loader
  def revoked_token_callback(jwt_header, jwt_payload: dict):
    return (
      jsonify(
        { "description": "The token has been revoked.", "error": "token_revoked"}
      ),
      401
    )
    
  @jwt.needs_fresh_token_loader
  def token_not_fresh_callback(jwt_header, jwt_payload):
    return (
      jsonify(
        {
          "description": "The token is not fresh.",
          "error": "fresh_token_required"
        }
      ),
      401
    )
  
  @app.after_request
  def refresh_expiring_jwts(response):
    try:
      exp_timestamp = get_jwt()["exp"]
      now = datetime.now(timezone.utc)
      target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
      if target_timestamp > exp_timestamp:
        access_token = create_access_token(identity=get_jwt_identity())
        set_access_cookies(response, access_token)
      return response
    except (RuntimeError, KeyError):
      return response

  with app.app_context():
    import schedule.models
    import auth.models
    db.create_all()

  api.register_blueprint(ShowsBlueprint)
  api.register_blueprint(EpisodesBlueprint)
  api.register_blueprint(UsersBlueprint)
  api.register_blueprint(InvitesBlueprint)
  
  return app
