from db import db
from lib.models import TimestampMixin

class EpisodeModel(TimestampMixin, db.Model):
  __tablename__ = "episodes"
  
  id = db.Column(db.Integer, primary_key=True)
  show_id = db.Column(
    db.Integer, 
    db.ForeignKey("shows.id"), 
    unique=False, nullable=False
  )
  show = db.relationship("ShowModel", back_populates="episodes")
  name = db.Column(db.String(100))
  date = db.Column(db.Date, nullable=False)


