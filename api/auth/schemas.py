from datetime import datetime
from marshmallow import ValidationError, fields, Schema, validate, validates
from sqlalchemy import select
from .models.user import UserModel
import re
from db import db

class UserSchema(Schema):
  id = fields.Int(dump_only=True)
  username = fields.Str(required=True, validate=validate.Length(min=1, max=30))
  password = fields.Str(required=True, validate=validate.Length(min=1, max=30), load_only=True)
  created_at = fields.DateTime(dump_only=True, load_default=datetime.now())
  email = fields.Email(required=True)
  is_admin = fields.Bool(load_default=False)
  

class UserRegisterSchema(UserSchema):
  class Meta:
    exclude = ["is_admin", "created_at"]
  
  @validates("email")
  def validates_email(self, email):
    stmt = select(UserModel).filter_by(email=email)
    if db.session.scalars(stmt).all():
      raise ValidationError("Email already registered.")
  
  @validates("username")
  def validates_username(self, username):
    if re.fullmatch(r"\w+", username) is None:
      raise ValidationError("Username may only contain letters, numbers and underscores.")
    stmt = select(UserModel).filter_by(username=username)
    if db.session.scalars(stmt).all():
      raise ValidationError("Username already registered.")
  
  @validates("password")
  def validates_password(self, password):
    if re.fullmatch(r"[\w\!\@\#\$\%\^\&\*]{8,}", password) is None:
      raise ValidationError("Passwords must be at least 8 characters, contain at least one number, and one special character (!, @, #, $, %, ^, &, *).")

class UserUpdateSchema(UserRegisterSchema):
  email = fields.Email(required=False)
  username = fields.Str(required=False, validate=validate.Length(min=1, max=30))
  is_admin = fields.Bool(required=False)
  
  class Meta:
    exclude = ["password"]

class UserLoginSchema(UserSchema):
  class Meta:
    fields = ["username", "password"]

class UserPasswordUpdateSchema(UserSchema):
  pass
  # class Meta:
  #   include = ["password"]
