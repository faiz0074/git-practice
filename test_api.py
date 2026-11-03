
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_status_code():
    response = requests.get(f"{BASE_URL}/users/1", timeout=10)
    assert response.status_code == 200

def test_user_name():
    response = requests.get(f"{BASE_URL}/users/1", timeout=10)
    data = response.json()
    assert data["name"] == "Leanne Graham"

def test_user_email():
    response = requests.get(f"{BASE_URL}/users/1", timeout=10)
    data = response.json()
    assert "@" in data["email"]

def test_invalid_user():
    response = requests.get(f"{BASE_URL}/users/9999", timeout=10)
    assert response.status_code == 404
