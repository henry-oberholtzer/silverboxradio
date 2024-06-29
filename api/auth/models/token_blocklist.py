from db import db
from lib.models import TimestampMixin

class TokenBlocklist(TimestampMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  jti = db.Column(db.String(36), nullable=False, index=True)
