from marshmallow import ValidationError
from sqlalchemy import select
from sqlalchemy.sql.operators import ilike_op

from auth.models.user import UserModel
from auth.models.invite import InviteModel

from db import db

def validate_email(model, message, email):
    stmt = select(model).filter(model.email.ilike(email))
    if db.session.scalars(stmt).all():
      raise ValidationError(message)

def validate_user_email(email):
  return validate_email(UserModel, "Email already registered.", email)

def validate_invite_email(email):
  return validate_email(InviteModel, "Email already invited.", email)

