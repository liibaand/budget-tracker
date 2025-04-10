import pytest
import time
from app import create_app
from config import TestConfig
from models import db

# Create a new app instance for testing with the in-memory DB
@pytest.fixture
def app_instance():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

# Client that uses the test app
@pytest.fixture
def client(app_instance):
    return app_instance.test_client()


def test_register(client):
    unique_username = f'testuser_{int(time.time())}'
    response = client.post('/register', json={
        'username': unique_username,
        'password': 'testpass'
    })
    assert response.status_code == 200
    assert response.json.get('message') == "User registered successfully!"


def test_login(client):
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass'
    })

    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == "Login successful"
    assert json_data['user_id'] is not None


def test_add_entry(client):
    client.post('/register', json={
        'username': 'testuser',
        'password': 'testpass'
    })

    login_response = client.post('/login', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    user_id = login_response.get_json()['user_id']

    response = client.post('/add', json={
        'category': 'Food & Dining',
        'amount': 50.00,
        'date': '2025-04-01',
        'user_id': user_id
    })

    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == "Entry added successfully!"
