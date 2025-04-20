import allure
import pytest
import requests
from helpers import generate_random_string, login_and_get_courier_id, delete_courier
from data import Url



class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера')
    @allure.description('Проверка получения кода 201 Created и сообщения {"ok": True} при отправке POST-запроса '
                        'на создание курьера при заполненных полях login, password и firstName валидными данными')
    def test_create_courier(self):
        payload = {'login': generate_random_string(10), 'password': generate_random_string(10),
                   'firstName': generate_random_string(10)}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Url.COURIER_CREATE_URL, json=payload, headers=headers)
        assert response.status_code == 201 and response.json() == {"ok": True}
        courier_id = login_and_get_courier_id(payload)
        delete_courier(courier_id)