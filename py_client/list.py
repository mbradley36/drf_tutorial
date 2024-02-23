import requests
from getpass import getpass

endpoint = "http://localhost:8000/api/auth/"
password = getpass()

get_response = requests.post(
    endpoint, json={"username": "user", "password": password})
print(get_response.json())

if (get_response.status_code == 200):
    token = get_response.json()['token']
    headers = {
        "Authorization": f"Token {token}"
    }
    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
