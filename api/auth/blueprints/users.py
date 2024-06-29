import string
from flask.views import MethodView
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from datetime import datetime
from flask_jwt_extended import jwt_required
from sqlalchemy import select
from lib.permissions import admin_only, is_user_or_admin
from db import db
from auth.models import UserModel, InviteModel
from auth.schemas import UserAccessSchema, UserLoginSchema, UserPasswordUpdateSchema, UserSchema, UserRegisterSchema, UserUpdateSchema

blp = Blueprint("Users", "users", description="Operations on users")

@blp.route("/register")
class UserRegister(MethodView):
  
  @blp.arguments(UserRegisterSchema)
  def post(self, user_data):
# Checks for an invite
    stmt= select(InviteModel).where(InviteModel.email == user_data["email"])
    if not db.session.scalars(stmt).all():
      abort(403, message="This email has not been invited.")
# If an invite is found, creates the user.
    user = UserModel(
      username=user_data["username"],
      email=user_data["email"],
      password=pbkdf2_sha256.hash(user_data["password"]),
      is_admin=False
    )
    db.session.add(user)
    db.session.commit()
    
    return {"message": "Registration successful."}, 201

@blp.route("/login")
class UserLogin(MethodView):
  
  @blp.arguments(UserLoginSchema)
  def post(self, user_data):
    user = UserModel.query.filter(
      UserModel.username == user_data["username"]
    ).first()
    
    if user and pbkdf2_sha256.verify(user_data["password"], user.password):
      access_token = create_access_token(identity=user.id)
      return { "access_token": access_token }, 200
    
    abort(401, message="Invalid credentials.")



@blp.route("/change-password")
class UserChangePassword(MethodView):
  
  @blp.arguments(UserPasswordUpdateSchema)
  @jwt_required()
  def put(self, password_data, user_id):
    is_user_or_admin(user_id)
    return { "Not implemented" }, 501

@blp.route("/users")
class UserList(MethodView):
  
  @blp.response(200, UserSchema(many=True))
  @jwt_required()
  def get(self):
    return UserModel.query.all()

@blp.route("/users/<int:user_id>")
class User(MethodView):
  
  @blp.response(200, UserSchema)
  @jwt_required()
  def get(self, user_id):
    user = db.get_or_404(UserModel, user_id)
    return user
  
  @blp.response(204)
  @jwt_required()
  def delete(self, user_id):
    is_user_or_admin(user_id)
    user = db.get_or_404(UserModel, user_id)
    db.session.delete(user)
    db.session.commit()
  
  @blp.arguments(UserUpdateSchema)
  @blp.response(200, UserSchema)
  @jwt_required()
  def put(self, user_data, user_id):
    is_admin = is_user_or_admin(user_id)
    
    user = db.get_or_404(UserModel, user_id)
    if user:
      if "username" in user_data:
        user.username = user_data["username"]
      if "email" in user_data:
        user.email = user_data["email"]
    else:
      user = UserModel(id=user_id, **user_data)
    
    db.session.add(user)
    db.session.commit()
    return user
  
@blp.route("/users/<int:user_id>/access")
class UserAccess(MethodView):

  @blp.arguments(UserAccessSchema)
  @blp.response(200, UserSchema)
  @jwt_required()
  def put(self, user_data, user_id):
    admin_only()
    
    user = db.get_or_404(UserModel, user_id)
    if user:
        user.is_admin = user_data["is_admin"]
    else:
      user = UserModel(id=user_id, **user_data)
    
    db.session.add(user)
    db.session.commit()
    return user
