from flask.views import MethodView
from flask_jwt_extended import create_access_token
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from datetime import datetime

from db import db
from auth.models import UserModel
from auth.schemas import UserLoginSchema, UserPasswordUpdateSchema, UserSchema, UserRegisterSchema, UserUpdateSchema

blp = Blueprint("Users", "users", description="Operations on users")

@blp.route("/register")
class UserRegister(MethodView):
  
  @blp.arguments(UserRegisterSchema)
  def post(self, user_data):
    
    user = UserModel(
      username=user_data["username"],
      email=user_data["email"],
      password=pbkdf2_sha256.hash(user_data["password"]),
      created_at=datetime.now(),
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
  def put(self, password_data, user_id):
    return { "Not implemented" }, 501

@blp.route("/users")
class UserList(MethodView):
  
  @blp.response(200, UserSchema(many=True))
  def get(self):
    return UserModel.query.all()

@blp.route("/users/<int:user_id>")
class User(MethodView):
  
  @blp.response(200, UserSchema)
  def get(self, user_id):
    user = db.get_or_404(UserModel, user_id)
    return user
  
  @blp.response(204)
  def delete(self, user_id):
    user = db.get_or_404(UserModel, user_id)
    db.session.delete(user)
    db.session.commit()
  
  @blp.arguments(UserUpdateSchema)
  @blp.response(200, UserSchema)
  def put(self, user_data, user_id):
    user = db.get_or_404(UserModel, user_id)
    if user:
      if "username" in user_data:
        user.username = user_data["username"]
      if "email" in user_data:
        user.email = user_data["email"]
      if "is_admin" in user_data:
        user.is_admin = user_data["is_admin"]
    else:
      user = UserModel(id=user_id, **user_data)
    
    db.session.add(user)
    db.session.commit()
    return user
      
