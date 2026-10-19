from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_normal_parameter():
    response = client.get("/users/10")

    assert response.status_code == 200
    assert response.json()["id"] == 10


def test_query_parameter():
    response = client.get("/users?name=John")

    assert response.status_code == 200
    assert response.json()["name"] == "John"




#To run ->>> pytest