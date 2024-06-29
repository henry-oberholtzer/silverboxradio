from sqlalchemy import func
from db import db

class TimestampMixin(object):
  created = db.Column(db.DateTime(timezone=True), server_default=func.now())
  updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

