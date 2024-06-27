from db import db

class UserModel(db.Model):
  __tablename__ = "users"
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(30), unique=True, nullable=False)
  email = db.Column(db.String(320), unique=True, nullable=False)
  password = db.Column(db.String(256), nullable=False)
  created_on = db.Column(db.DateTime, nullable=False)
  is_admin = db.Column(db.Boolean, nullable=False)


