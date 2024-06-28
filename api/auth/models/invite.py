from db import db
from sqlalchemy import func

class InviteModel(db.Model):
  __tablename__ = "invites"
  
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(320), unique=True, nullable=False)
  owner_id = db.Column(db.Integer, db.ForeignKey("users.id"),
    unique=False,
    nullable=False)
  owner = db.relationship("UserModel", back_populates="invites")
  created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
