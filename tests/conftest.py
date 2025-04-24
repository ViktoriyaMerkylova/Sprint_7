import requests
import generators
import pytest
import string
from data import Url

@pytest.fixture
def create_courier():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    creation_courier_body = {'login': login, 'password': password, 'first_name': name}
    login_courier_body = {'login': login, 'password': password}
    response = requests.post(Url.COURIER_CREATE_URL, json=creation_courier_body)
    assert response.status_code == 201, f"Failed to create courier: {response.text}"
    yield [creation_courier_body, login_courier_body, login, password]
    login_courier = requests.post(f'{Url.COURIER_LOGIN_URL}', json=login_courier_body)
    requests.delete(f'{Url.COURIER_CREATE_URL}/{login_courier.json()["id"]}')


@pytest.fixture
def create_courier_new():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    creation_courier_body = {'login': login, 'password': password, 'first_name': name}
    login_courier_body = {'login': login, 'password': password}
    yield [creation_courier_body, login_courier_body]
    login_courier = requests.post(f'{Url.COURIER_LOGIN_URL}', json=login_courier_body)
    requests.delete(f'{Url.COURIER_CREATE_URL}/{login_courier.json()["id"]}')

@pytest.fixture
def create_courier_two():
    login = generators.login_generator()
    password = generators.password_generator()
    create_courier_body = {'login': login, 'password': password}
    login_courier_body = {'login': login, 'password': password}
    yield [create_courier_body, login_courier_body, login, password]
    login_courier = requests.post(f'{Url.COURIER_LOGIN_URL}', json=login_courier_body)
    requests.delete(f'{Url.COURIER_CREATE_URL}/{login_courier.json()["id"]}')

@pytest.fixture
def create_courier_repeat():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    create_courier_body = {'login': login, 'password': password, 'first_name': name}
    login_courier_body = {'login': login, 'password': password}
    requests.post(f'{Url.COURIER_CREATE_URL}', json=create_courier_body)
    login_courier = requests.post(f'{Url.COURIER_LOGIN_URL}', json=login_courier_body)
    yield [create_courier_body, login_courier_body, login, password]
    requests.delete(f'{Url.COURIER_CREATE_URL}/{login_courier.json()["id"]}')
