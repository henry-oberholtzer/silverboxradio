import pytest
from flask.testing import FlaskClient

@pytest.fixture
def episode_setup(client: FlaskClient, auth):
  with client:
    client.post("/shows",
    headers=auth,
    json={
      "name": "test",
      "description": "test description",
      "duration": 2.0
    })  
    
def test_episode_post(client: FlaskClient, episode_setup, auth):
  with client:
    r = client.post("/episodes", headers=auth, json={
      "show_id": 1,
      "name": "episode",
      "date": "2024-06-26"
    })
    assert r.status_code == 201

def test_episode_post_show_doesnt_exist(client: FlaskClient, auth):
  with client:
    s = client.get("/shows/1")
    assert s.status_code == 404
    r = client.post("/episodes", headers=auth, json={
      "show_id": 1,
      "name": "episode",
      "date": "2024-06-26"
    })
    errors = r.get_json()["errors"]["json"]
    assert r.status_code == 422
    assert errors["show_id"][0] == "Show does not exist."
    
def test_episode_post_invalid_name(client: FlaskClient, episode_setup, auth):
  with client:
    r = client.post("/episodes", headers=auth, json={
        "show_id": 1,
        "name": f"{"a" * 101}",
        "date": "2024-06-26"
      })
    errors = r.get_json()["errors"]["json"]
    assert r.status_code == 422
    assert errors["name"][0] == 'Length must be between 1 and 100.'

def test_episode_post_invalid_date(client: FlaskClient, episode_setup):
  with client:
    r = client.post("/episodes", json={
          "show_id": 1,
          "name": "show",
          "date": "2024-56-26"
        })
    errors = r.get_json()["errors"]["json"]
    assert r.status_code == 422
    assert errors["date"][0] == 'Not a valid date.'
    
def test_episode_get_all(client: FlaskClient, episode_setup):
  with client:
    client.post("/episodes", json={
          "show_id": 1,
          "name": "show",
          "date": "2024-06-26"
        })
    client.post("/episodes", json={
          "show_id": 1,
          "name": "show 2",
          "date": "2024-06-26"
        })
    r = client.get("/episodes")
    assert r.status_code == 200

def test_episode_get_by_id(client: FlaskClient, episode_setup, auth):
  with client:
    client.post("/episodes", headers=auth, json={
          "show_id": 1,
          "name": "show",
          "date": "2024-06-26"
        })
    r = client.get("/episodes/1")
    assert r.status_code == 200

def test_episode_get_dne(client: FlaskClient):
  r = client.get("/episodes/1")
  assert r.status_code == 404

def test_episode_put_valid(client: FlaskClient, episode_setup, auth):
  with client:
    client.post("/episodes", headers=auth, json={
      "show_id": 1,
      "name": "show",
      "date": "2024-06-26"
    })
    r = client.put("/episodes/1", headers=auth, json={
      "show_id": 1,
      "name": "episode",
      "date": "2024-06-26"
    })
    assert r.status_code == 200

def test_episode_put_invalid(client: FlaskClient, episode_setup, auth):
  with client:
    client.post("/episodes", headers=auth, json={
      "show_id": 1,
      "name": "show",
      "date": "2024-06-26"
    })
    r = client.put("/episodes/1", headers=auth, json={
      "show_id": 2,
      "name": "episode",
      "date": "2024-06-26"
    })
    assert r.status_code == 422

def test_episode_delete(client: FlaskClient, episode_setup, auth):
  with client:
    client.post("/episodes", headers=auth, json={
      "show_id": 1,
      "name": "show",
      "date": "2024-06-26"
    })
    r = client.delete("/episodes/1", headers=auth)
    assert r.status_code == 204
