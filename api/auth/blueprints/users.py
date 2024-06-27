from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256

from db import db
from auth.models import UserModel
from auth.schemas import UserSchema, UserRegisterSchema

blp = Blueprint("Users", "users", description="Operations on users")

@blp.route("/register")
class UserRegister(MethodView):
  
  @blp.arguments(UserRegisterSchema)
  def post(self, user_data):
    if UserModel.query.filter(UserModel.username == user_data["username"]).first():
      abort(409, message="A user with that username already exists.")
    if UserModel.query.filter(UserModel.email == user_data["email"]).first():
      abort(409, message="This email is already in use.") 
    
    user = UserModel(
      username=user_data["username"],
      password=pbkdf2_sha256.hash(user_data["password"]),
    )
    db.session.add(user)
    db.session.commit()
    
    return {"message": "Registration successful."}, 201

@blp.route("/users")
class UserList(MethodView):
  
  @blp.response(200, UserSchema)
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
  
  @blp.arguments(UserSchema)
  @blp.response(200, UserSchema)
  def put(self, user_data, user_id):
    user = db.get_or_404(UserModel, user_id)
    if user:
      user.username = user_data["username"]
      user.email = user_data["email"]
      
