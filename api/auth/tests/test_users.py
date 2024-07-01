from flask.testing import FlaskClient
import pytest


@pytest.fixture
def register_user(client: FlaskClient, admin):
  with client:
    client.post("/invites", headers=admin, json={
      "email": "test@henryoberholtzer.com"
    })
    r = client.post("/register", json={
      "username": "test",
      "password": "t3st_password!",
      "email": "test@henryoberholtzer.com",
    })

def test_user_post(client: FlaskClient, admin):
  with client:
    invite = client.post("/invites", headers=admin, json={
      "email": "test@henryoberholtzer.com"
    })
    assert invite.status_code == 201
    r = client.post("/register", json={
      "username": "test",
      "password": "t3st_password!",
      "email": "test@henryoberholtzer.com",
    })
    assert r.status_code == 201

def test_user_post_no_invite(client: FlaskClient):
  with client:
    r = client.post("/register", json={
      "username": "test",
      "password": "t3st_password!",
      "email": "test@henryoberholtzer.com",
    })
    assert r.status_code == 403

def test_user_post_email_duplicate(client: FlaskClient, register_user):
  with client:
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

def test_user_post_username_duplicate(client: FlaskClient, register_user):
  with client:
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

def test_user_login(client: FlaskClient, register_user):
  with client:
    r = client.post("/login", json={
      "username": "test",
      "password": "t3st_password!",
    })
    assert r.status_code == 200

def test_user_login_invalid(client: FlaskClient, register_user):
  with client:
    r = client.post("/login", json={
      "username": "test",
      "password": "tst_password!",
    })
    assert r.status_code == 401

def test_user_get_all(client: FlaskClient, auth):
  with client:
    r = client.get("/users", headers=auth)
    assert r.get_json()[0]["username"] == "admin"
    assert r.get_json()[1]["username"] == "user"

def test_user_get_by_id(client: FlaskClient, auth):
  with client:
    r = client.get("/users/2", headers=auth)
    assert r.get_json()["username"] == "user"

def test_user_get_by_id_dne(client: FlaskClient, auth):
  with client:
    r = client.get("/users/3", headers=auth)
    assert r.status_code == 404

def test_user_delete(client: FlaskClient, auth):
  with client:
    r = client.delete("/users/2", headers=auth)
    assert r.status_code == 200

def test_put_user_username(client: FlaskClient, auth):
  with client:
    r = client.put("/users/2", headers=auth, json={
      "username": "henry",
    })
    assert r.status_code == 200
    assert r.get_json()["username"] == "henry"

def test_put_user_username_invalid(client: FlaskClient, auth):
  with client:
    r = client.put("/users/2", headers=auth, json={
      "username": "henry!",
    })
    assert r.status_code == 422

def test_put_user_username_and_email(client: FlaskClient, auth):
  with client:
    r = client.put("/users/2", headers=auth, json={
      "username": "henry",
      "email": "mynewemail@email.com"
    })
    assert r.status_code == 200
    assert r.get_json()["username"] == "henry"
    assert r.get_json()["email"] == "mynewemail@email.com"

def test_set_user_admin(client: FlaskClient, admin, register_user):
  with client:
    r = client.put("/users/2/access", headers=admin, json={
      "is_admin": True,
    })
    assert r.status_code == 200
    assert r.get_json()["is_admin"] == True

def test_set_user_admin_non_admin(client: FlaskClient, auth):
  with client:
    r = client.put("/users/2/access", headers=auth, json={
      "is_admin": True,
    })
    assert r.status_code == 401
    
def test_only_allow_user_to_adjust_profile(client: FlaskClient, register_user):
  with client:
    client.post("/register", json={
      "username": "test_auth",
      "password": "t3st_password!",
      "email": "test1@henryoberholtzer.com",
    })
    auth_user = client.post("/login", json={
      "username": "test_auth",
      "password": "t3st_password!"
    })
    r = client.put("/users/1", headers=auth_user.get_json(), json={
      "username": "change_that",  
    })
    assert r.status_code == 401

def test_user_logout(client: FlaskClient, auth):
  with client:
    r = client.get("/users/2", headers=auth)
    assert r.status_code == 200
    z = client.post("/logout", headers=auth)
    assert z.status_code == 200
    r = client.get("/users/2", headers=auth)
    assert r.status_code == 401
