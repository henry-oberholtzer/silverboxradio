from flask import Flask
from flask.testing import FlaskClient
from auth.models.user import UserModel
from db import db
from passlib.hash import pbkdf2_sha256
import pytest
from app import create_app

@pytest.fixture()
def app():
  db_url = "sqlite:///test.db"
  app = create_app(db_url)
  app.config.update({
    "TESTING": True,
  })
  with app.app_context():
    db.create_all()
    yield app
    db.session.remove()
    db.drop_all()
  

@pytest.fixture()
def client(app: Flask):
  return app.test_client()

@pytest.fixture()
def runner(app: Flask):
  return app.test_cli_runner()

@pytest.fixture()
def auth(client: FlaskClient):
  with client:
    client.post("/register", json={
      "username": "user",
      "password": "t3st_password!",
      "email": "user@henryoberholtzer.com",
    })
    r = client.post("/login", json={
      "username": "user",
      "password": "t3st_password!",
    })
    token = r.get_json()["access_token"]
    return {
      "Authorization": f"Bearer {token}",
    }

@pytest.fixture
def admin(client: FlaskClient):
  with client:
    admin = UserModel(
      username="admin",
      email="admin@admin.com",
      password=pbkdf2_sha256.hash("admin"),
      is_admin=True
    )
    db.session.add(admin)
    db.session.commit()
    r = client.post("/login", json={
      "username": "admin",
      "password": "admin"
    })
    token = r.get_json()["access_token"]
    return {
      "Authorization": f"Bearer {token}",
    }
