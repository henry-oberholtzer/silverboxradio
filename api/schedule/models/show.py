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

