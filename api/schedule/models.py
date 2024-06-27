from db import db

class ShowModel(db.Model):
  __tablename__ = "shows"
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(500))
  duration = db.Column(db.Integer)
  episodes = db.relationship("EpisodeModel", 
    back_populates="show", 
    lazy="dynamic",
    cascade="all, delete")

class EpisodeModel(db.Model):
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


