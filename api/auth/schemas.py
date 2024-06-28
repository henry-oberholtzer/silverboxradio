from datetime import datetime
from marshmallow import ValidationError, fields, Schema, validate, validates
from sqlalchemy import select
from .models.user import UserModel
import re
from db import db
from lib.validators import validate_email, validate_invite_email, validate_user_email

class UserSchema(Schema):
  id = fields.Int(dump_only=True)
  username = fields.Str(required=True, validate=validate.Length(min=1, max=30))
  password = fields.Str(required=True, validate=validate.Length(min=1, max=30), load_only=True)
  created_at = fields.DateTime(dump_only=True)
  updated_at = fields.DateTime(dump_only=True)
  email = fields.Email(required=True, validate=validate_user_email)
  is_admin = fields.Bool(load_default=False)
  

class UserRegisterSchema(UserSchema):
  class Meta:
    exclude = ["is_admin", "created_at"]
  
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
    
class UserPublicSchema(UserSchema):
  class Meta:
    fields = ["id", "username", "is_admin"]

class UserLoginSchema(UserSchema):
  class Meta:
    fields = ["username", "password"]

class UserPasswordUpdateSchema(UserSchema):
  pass
  # class Meta:
  #   include = ["password"]

class InviteSchema(Schema):
  id = fields.Int(dump_only=True)
  email = fields.Email(required=True, validate=validate_invite_email)
  owner = fields.Nested(UserPublicSchema(), dump_only=True)
  owner_id = fields.Int(required=True)
  created_at = fields.DateTime(dump_only=True)

class InvitePostSchema(Schema):
  email = fields.Email(required=True, validate=validate_invite_email)
