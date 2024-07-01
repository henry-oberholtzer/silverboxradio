from flask import Flask
from flask.testing import FlaskClient
from auth.models.user import UserModel
from db import db
from passlib.hash import pbkdf2_sha256
import pytest
from app import create_app
from flask_jwt_extended import create_access_token

@pytest.fixture()
def app():
  app = create_app(config="config.TestingConfig")
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
    token = create_access_token(admin.id, fresh=True)
    return {
      "Authorization": f"Bearer {token}",
    }

@pytest.fixture()
def auth(client: FlaskClient, admin):
  with client:
    client.post("/invites", headers=admin, json={
      "email": "user@henryoberholtzer.com"
    })
    r = client.post("/register", json={
      "username": "user",
      "password": "t3st_password!",
      "email": "user@henryoberholtzer.com",
    })
    token = create_access_token(r.get_json()["id"], fresh=True)
    return {
      "Authorization": f"Bearer {token}",
    }


