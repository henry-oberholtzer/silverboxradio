import pytest
from flask.testing import FlaskClient

@pytest.fixture
def episode_setup(client: FlaskClient):
  with client:
    client.post("/shows", json={
      "name": "test",
      "description": "test description",
      "duration": 2.0
    })  
    
def test_episode_post(client: FlaskClient, episode_setup):
  with client:
    r = client.post("/episodes", json={
      "show_id": 1,
      "name": "episode",
      "date": "2024-06-26"
    })
    assert r.status_code == 201

def test_episode_post_show_doesnt_exist(client: FlaskClient):
  with client:
    s = client.get("/shows/1")
    print(s.get_json())
    assert s.status_code == 404
    r = client.post("/episodes", json={
      "show_id": 1,
      "name": "episode",
      "date": "2024-06-26"
    })
    errors = r.get_json()["errors"]["json"]
    assert r.status_code == 422
    assert errors["show_id"][0] == "Show does not exist."
    
def test_episode_post_invalid_name(client: FlaskClient, episode_setup):
  with client:
    r = client.post("/episodes", json={
        "show_id": 1,
        "name": f"{"a" * 101}",
        "date": "2024-06-26"
      })
    errors = r.get_json()["errors"]["json"]
    assert r.status_code == 422
    assert errors["name"][0] == 'Length must be between 1 and 100.'

# def test_episode_post_invalid_date(client: FlaskClient):
#   pass

# def test_episode_post_show_doesnt_exist(client: FlaskClient):
#   pass

# def test_episode_get_all(client: FlaskClient):
#   pass

# def test_episode_get_by_id(client: FlaskClient):
#   pass

# def test_episode_get_dne(client: FlaskClient):
#   pass

# def test_episode_put_valid(client: FlaskClient):
#   pass

# def test_episode_put_invalid(client: FlaskClient):
#   pass

# def test_episode_delete(client: FlaskClient):
#   pass
