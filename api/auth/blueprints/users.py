import string
from flask import Response, jsonify
from flask.views import MethodView
from flask_jwt_extended import (
  create_access_token,
  set_access_cookies,
  set_refresh_cookies, 
  get_jwt,
  create_refresh_token,
  unset_jwt_cookies)
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import jwt_required
from sqlalchemy import select
from lib.permissions import admin_only, is_user_or_admin
from db import db
from auth.models import UserModel, InviteModel, TokenBlocklist
from auth.schemas import UserAccessSchema, UserLoginSchema, UserPasswordUpdateSchema, UserSchema, UserRegisterSchema, UserUpdateSchema

blp = Blueprint("Users", "users", description="Operations on users")

@blp.route("/register")
class UserRegister(MethodView):
  
  @blp.arguments(UserRegisterSchema)
  @blp.response(201, UserSchema)
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
    
    return user

@blp.route("/login")
class UserLogin(MethodView):
  
  @blp.response(200, UserSchema)
  @blp.arguments(UserLoginSchema)
  def post(self, user_data):
    user: UserModel = UserModel.query.filter(
      UserModel.username == user_data["username"]
    ).first()
    
    if user and pbkdf2_sha256.verify(user_data["password"], user.password):
      additional_claims = { "is_admin": user.is_admin }
      access_token = create_access_token(identity=user.id, additional_claims=additional_claims, fresh=True)
      refresh_token = create_refresh_token(user.id)
      response = jsonify({ 
        "access_token": access_token,
        "refresh_token": refresh_token
        })
      set_access_cookies(response, access_token)
      set_refresh_cookies(response, refresh_token)
      return user
    
    abort(401, message="Invalid credentials.")

@blp.route("/logout")
class UserLogout(MethodView):
  
  @jwt_required()
  @blp.response(200)
  def post(self):
    response = jsonify({ "message": "Logout successful."})
    jti = get_jwt()["jti"]
    db.session.add(TokenBlocklist(jti=jti))
    db.session.commit()
    unset_jwt_cookies(response)
    return response

@blp.route("/change-password")
class UserChangePassword(MethodView):
  
  @blp.arguments(UserPasswordUpdateSchema)
  @jwt_required(fresh=True)
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
  
  @blp.response(200)
  @jwt_required(fresh=True)
  def delete(self, user_id):
    is_user_or_admin(user_id)
    user = db.get_or_404(UserModel, user_id)
    response = jsonify({ "message": f"Account <{user.email}> deleted."})
    db.session.delete(user)
    db.session.commit()
    return response
  
  @blp.arguments(UserUpdateSchema)
  @blp.response(200, UserSchema)
  @jwt_required()
  def put(self, user_data, user_id):
    is_user_or_admin(user_id)
    
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
  @jwt_required(fresh=True)
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
