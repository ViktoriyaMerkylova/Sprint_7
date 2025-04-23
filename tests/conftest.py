import requests
import generators
import string
from data import Url, Registration
import pytest

@pytest.fixture
def create_courier():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    create_courier_body = {'login': login, 'password': password, 'first_name': name}
    login_courier_body = {'login': login, 'password': password}
    yield [create_courier_body, login_courier_body, login, password]
    login_response = requests.post(f'{Url.COURIER_LOGIN_URL}', json=login_courier_body)
    requests.delete(f'{Url.COURIER_CREATE_URL}/{login_response.json()["id"]}')

@pytest.fixture
def create_courier_two():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    create_courier_body = {'login': login, 'password': password}
    login_courier_body = {'login': login, 'password': password}
    yield [create_courier_body, login_courier_body, login, password]
    login_response = requests.post(f'{Url.COURIER_LOGIN_URL}', json=login_courier_body)
    requests.delete(f'{Url.COURIER_CREATE_URL}/{login_response.json()["id"]}')