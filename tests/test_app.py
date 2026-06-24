from conftest import client
def test_create_member(client):
    response = client.post("/member" , json = {"id":"45" , "name":"ryan" , "credit":900})
    assert response.status_code == 201
    assert response.get_json()["message"] == "successfully registered"
def test_duplicate(client):
    payload = {"id":"67" , "name":"lucy" , "credit": 900}
    client.post("/member" ,json=payload)
    response = client.post("/member",json=payload)
    assert response.status_code == 409
    assert response.get_json()["message"] == "user already exists"
    print(response.status_code)
    print(response.get_json())