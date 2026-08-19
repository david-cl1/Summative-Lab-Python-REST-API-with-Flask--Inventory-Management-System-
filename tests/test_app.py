import pytest
from app import app
from unittest.mock import patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_inventory(client):
    res = client.get('/inventory')
    assert res.status_code == 200

def test_add_item(client):
    payload = {"product_name": "Test Item", "brand": "Generic", "price": 1.99, "stock": 5}
    res = client.post('/inventory', json=payload)
    assert res.status_code == 201
    assert res.json["product_name"] == "Test Item"

def test_update_item(client):
    res = client.patch('/inventory/1', json={"price": 6.00})
    assert res.status_code == 200
    assert res.json["price"] == 6.00

def test_delete_item(client):
    res = client.delete('/inventory/1')
    assert res.status_code == 200

@patch('app.requests.get')
def test_external_api_mock(mock_get, client):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {"product_name": "Mocked Nutella", "brands": "Ferrero"}
    }
    res = client.post('/inventory/external/0056195003005', json={"price": 4.00, "stock": 10})
    assert res.status_code == 201
    assert res.json["item"]["product_name"] == "Mocked Nutella"