import pytest
from flask.testing import FlaskClient

def test_invite_post(client: FlaskClient, admin):
  with client:
    r = client.post("/invites", headers=admin, json={
      "email": "email@email.com"
    })
    assert r.status_code == 201
    print(r.get_json())
    assert r.get_json()["email"] == "email@email.com"

def test_invite_post_invalid(client: FlaskClient, admin):
  with client:
    r = client.post("/invites", headers=admin, json={
      "email": "email.email.com"
    })
    assert r.status_code == 422

def test_invite_post_duplicate(client: FlaskClient, admin):
  with client:
    client.post("/invites", headers=admin, json={
      "email": "email@email.com"
    })
    r = client.post("/invites", headers=admin, json={
      "email": "email@email.com"
    })
    assert r.status_code == 422

def test_invite_post_close_duplicate(client: FlaskClient, admin):
  with client:
    client.post("/invites", headers=admin, json={
      "email": "email@email.com"
    })
    r = client.post("/invites", headers=admin, json={
      "email": "EMAIL@email.com"
    })
    print(r.get_json())
    assert r.status_code == 422

def test_invite_post_close_duplicate(client: FlaskClient, admin):
  with client:
    client.post("/invites", headers=admin, json={
      "email": "Email@email.com"
    })
    r = client.post("/invites", headers=admin, json={
      "email": "email@email.com"
    })
    print(r.get_json())
    assert r.status_code == 422
