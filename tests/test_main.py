from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI App"}


def test_create_item():
    item_data = {"name": "Test Item", "price": 10.99, "description": "A test item"}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json()["item"] == item_data
    assert response.json()["message"] == "Item created succesfully"