from flask.testing import FlaskClient

def test_get_shows(client: FlaskClient):
  with client:
    response = client.get("/shows")
    assert response.status_code == 200

def test_post_show(client: FlaskClient):
  with client:
    response = client.post("/shows", json={
      "name": "test",
      "description": "test description",
      "duration": 2.0
    })
    json = response.get_json()
    assert response.status_code == 201
    assert json["id"] == 1

def test_post_show_name_too_long(client: FlaskClient):
  with client:
    response = client.post("/shows", json={
      "name": f"{'a' * 101}",
      "description": "test description",
      "duration": 2.0
    })
    assert response.status_code == 422

def test_show_post_desc_too_long(client: FlaskClient):
  with client:
    response = client.post("/shows", json={
      "name": "test",
      "description":  f"{'a' * 501}",
      "duration": 2.0
    })
    assert response.status_code == 422

def test_delete_show(client: FlaskClient):
  with client:
    response = client.post("/shows", json={
      "name": "test",
      "description": "test description",
      "duration": 2.0
    })
    assert response.status_code == 201
    delete = client.delete("/shows/1")
    assert delete.status_code == 204

def test_put_show(client: FlaskClient):
  with client:
    response = client.post("/shows", json={
      "name": "test",
      "description": "test description",
      "duration": 2.0
    })
    assert response.status_code == 201
    put = client.put("/shows/1", json={
      "name": "testing",
      "description": "test description",
      "duration": 2.0
    })
    result = put.get_json()
    print(put.get_json())
    assert put.status_code == 200
    assert result['name'] == "testing"

def test_put_show_invalid_fields(client: FlaskClient):
  with client:
    response = client.post("/shows", json={
      "name": "test",
      "description": "test description",
      "duration": 2.0
    })
    assert response.status_code == 201
    put = client.put("/shows/1", json={
      "name": f"{'a' * 101}",
      "description": f"{'a' * 501}",
      "duration": 2.0
    })
    result = put.get_json()['errors']['json']
    print(put.get_json())
    assert put.status_code == 422
    assert result['name'][0] == 'Length must be between 1 and 100.'
    assert result['description'][0] == 'Longer than maximum length 500.'


def test_get_show_by_id(client: FlaskClient):
  with client:
    response = client.post("/shows", json={
      "name": "test",
      "description": "test description",
      "duration": 2.0
    })
    json = response.get_json()
    get = client.get("/shows/1").get_json()
    assert get == json

def test_get_show_by_id_doesnt_exist(client: FlaskClient):
  with client:
    get = client.get("/shows/1")
    assert get.status_code == 404

def test_delete_show_by_id_doesnt_exist(client: FlaskClient):
  with client:
    get = client.delete("/shows/1")
    assert get.status_code == 404
