from datetime import datetime
from marshmallow import fields, Schema, validate

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

class UserUpdateSchema(UserSchema):
  class Meta:
    exclude = ["id", "created_at", "password"]

class UserPasswordUpdateSchema(UserSchema):
  pass
  # class Meta:
  #   include = ["password"]
