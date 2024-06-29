from db import db
from lib.models import TimestampMixin

class InviteModel(TimestampMixin, db.Model):
  __tablename__ = "invites"
  
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(320), unique=True, nullable=False)
  owner_id = db.Column(db.Integer, db.ForeignKey("users.id"),
    unique=False,
    nullable=False)
  owner = db.relationship("UserModel", back_populates="invites")
