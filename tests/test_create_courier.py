import allure
import pytest
import requests
from helpers import generate_random_string
from data import Url, ResponseBody


class TestCreateCourier:
    @allure.title('Проверка успешного: создания курьера, возвращение правильного кода ответа и {"ok": True}')
    @allure.description('Проверка получения кода 201 Created, создание курьера и сообщения {"ok": True} при отправке POST-запроса '
                        'на создание курьера при заполненных полях login, password и firstName валидными данными')
    def test_create_courier(self, create_courier_new):
        registration = requests.post(f'{Url.COURIER_CREATE_URL}', json=create_courier_new[0])
        assert registration.status_code == 201 and (registration.json() == ResponseBody.COURIER_CREATION_SUCCESS)

    @allure.title('Проверка невозможности создания 2х одинаковых курьеров и возвращении ошибки')
    @allure.description('Проверка получения кода 409 Conflict и сообщения '
                        '{"message": "Этот логин уже используется. Попробуйте другой."} при отправке POST-запроса на создание курьера '
                        'при использовании существующего логина')
    def test_create_courier_сonflicts(self, create_courier_repeat):
        response = requests.post(f'{Url.COURIER_CREATE_URL}', json=create_courier_repeat[0])
        assert response.status_code == 409 and (response.json() == ResponseBody.COURIER_NAME_ALREADY_EXIST)

    @allure.title('Проверка успешного создания курьера только при заполненных обязательных полей, возвращения правильного кода ответа и {"ok":true}')
    @allure.description('Проверка получения кода 201 Created, создание курьера и сообщения {"ok": True} при отправке POST-запроса '
                        'на создание курьера при заполненных полях login и password валидными данными')
    def test_create_courier_required_fields_filled_in_success(self, create_courier_two):
        registration = requests.post(f'{Url.COURIER_CREATE_URL}', json=create_courier_two[0])
        assert registration.status_code == 201 and (registration.json() == ResponseBody.COURIER_CREATION_SUCCESS)

    @allure.title('Проверка неудачного создания курьера при незаполненном поле')
    @allure.description('Проверка получения кода 400 Bad request и сообщения '
                        '{"message": "Недостаточно данных для создания учетной записи"} при отправке POST-запроса '
                        'на создание курьера при незаполненных полях login/password')
    @pytest.mark.parametrize('login,password', [
        ('', generate_random_string(10)),
        (generate_random_string(10), '')
    ])
    def test_create_courier_without_required_fields_failed(self, login, password):
        payload = {'login': login, 'password': password}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Url.COURIER_CREATE_URL, json=payload, headers=headers)
        assert response.status_code == 400 and response.json() == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA
