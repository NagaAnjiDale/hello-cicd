
from app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_greeting():
    client = app.test_client()
    response = client.get("/greeting/World")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}
