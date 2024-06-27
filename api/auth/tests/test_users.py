from flask.testing import FlaskClient
import pytest

def test_user_post(client: FlaskClient):
  with client:
    r = client.post("/register", json={
      "username": "test",
      "password": "t3st_password!",
      "email": "test@henryoberholtzer.com",
    })
    assert r.status_code == 201

def test_user_post_email_duplicate(client: FlaskClient):
  with client:
    r = client.post("/register", json={
      "username": "test",
      "password": "t3st_password!",
      "email": "test@henryoberholtzer.com",
    })
    assert r.status_code == 201
    s = client.post("/register", json={
      "username": "test_2",
      "password": "t3st_password!",
      "email": "test@henryoberholtzer.com",
    })
    errors = s.get_json()["errors"]["json"]
    assert errors["email"][0] == "Email already registered."
    assert s.status_code == 422

def test_user_post_email_invalid(client: FlaskClient):
  with client:
    r = client.post("/register", json={
      "username": "test",
      "password": "t3st_password!",
      "email": "test@henryoberholtzercom",
    })
    errors = r.get_json()["errors"]["json"]
    assert errors["email"][0] == 'Not a valid email address.'
    assert r.status_code == 422

def test_user_post_username_duplicate(client: FlaskClient):
  with client:
    r = client.post("/register", json={
      "username": "test",
      "password": "t3st_password!",
      "email": "test@henryoberholtzer.com",
    })
    assert r.status_code == 201
    s = client.post("/register", json={
      "username": "test",
      "password": "t3st_password!",
      "email": "test2@henryoberholtzer.com",
    })
    errors = s.get_json()["errors"]["json"]
    assert errors["username"][0] == "Username already registered."
    assert s.status_code == 422

def test_user_post_username_invalid_chars(client: FlaskClient):
  with client:
    s = client.post("/register", json={
      "username": "test!!!",
      "password": "t3st_password!",
      "email": "test2@henryoberholtzer.com",
    })
    errors = s.get_json()["errors"]["json"]
    assert errors["username"][0] == "Username may only contain letters, numbers and underscores."
    assert s.status_code == 422

def test_user_post_username_invalid_length(client: FlaskClient):
  with client:
    s = client.post("/register", json={
      "username": "test!!!",
      "password": "t3st_password!",
      "email": "test2@henryoberholtzer.com",
    })
    errors = s.get_json()["errors"]["json"]
    assert errors["username"][0] == "Username may only contain letters, numbers and underscores."
    assert s.status_code == 422

def test_user_post_password_insecure(client: FlaskClient):
  with client:
    s = client.post("/register", json={
      "username": "test",
      "password": "mydog",
      "email": "test2@henryoberholtzer.com",
    })
    errors = s.get_json()["errors"]["json"]
    assert errors["password"][0] == "Passwords must be at least 8 characters, contain at least one number, and one special character (!, @, #, $, %, ^, &, *)."
    assert s.status_code == 422
