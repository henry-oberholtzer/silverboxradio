from db import db
from lib.models import TimestampMixin

class UserModel(TimestampMixin, db.Model):
  __tablename__ = "users"
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(30), unique=True, nullable=False)
  email = db.Column(db.String(320), unique=True, nullable=False)
  password = db.Column(db.String, nullable=False)
  is_admin = db.Column(db.Boolean, nullable=False)
  invites = db.relationship("InviteModel",
    back_populates="owner",
    lazy="dynamic",
    cascade="all, delete")
  
  def __str__(self) -> str:
    return f"User: {self.username}"

