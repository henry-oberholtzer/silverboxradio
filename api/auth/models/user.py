from db import db
from sqlalchemy import func
from sqlalchemy.orm import column_property, validates

class UserModel(db.Model):
  __tablename__ = "users"
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(30), unique=True, nullable=False)
  email = db.Column(db.String(320), unique=True, nullable=False)
  password = db.Column(db.String, nullable=False)
  created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
  updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
  is_admin = db.Column(db.Boolean, nullable=False)
  invites = db.relationship("InviteModel",
    back_populates="owner",
    lazy="dynamic",
    cascade="all, delete")

