from fastapi.testclient import TestClient


def test_root(app):
    client = TestClient(app)
    response = client.get("/dummy")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
