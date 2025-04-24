import requests
import random
import string
from data import Url


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def login_and_get_courier_id(payload):
    login_response = requests.post(Url.COURIER_LOGIN_URL, json=payload)
    assert login_response.status_code == 200
    courier_id = login_response.json().get('id')
    assert courier_id is not None
    return courier_id
