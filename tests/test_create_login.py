import allure
import pytest
import requests
from helpers import register_new_courier_and_return_login_password, generate_random_string, delete_courier
from data import Url, login_valid, password_valid


class TestCreateLogin:
    @allure.title('Проверка возможности авторизации курьера и необходимости передачи всех обязательных полей')
    @allure.description('Проверка получения кода 200 Ok и сообщения {"id": [___]} при отправке POST-запроса '
                        'на авторизацию курьера при заполненных полях login и password валидными данными')
    def test_login_courier(self):
        create_login = register_new_courier_and_return_login_password()
        login, password, first_name = create_login
        payload = {'login': login, 'password': password}
        response = requests.post(Url.COURIER_LOGIN_URL, data=payload)
        assert response.status_code == 200 and 'id' in response.json()
        courier_id = response.json().get('id')
        delete_courier(courier_id)


    @allure.title('Проверка ошибки, если неправильно указать логи или пароль')
    @allure.description('Проверка получения кода 404 Not found и сообщения '
                        '{"message": "Учетная запись не найдена"} при отправке POST-запроса '
                        'на авторизацию курьера при несуществующем login и некорректном password')
    @pytest.mark.parametrize('login, password', [
        (generate_random_string(10), password_valid),
        (login_valid, generate_random_string(10))
    ])
    def test_login_courier_with_incorrect_data(self, login, password):
        payload = {'login': login, 'password': password}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Url.COURIER_LOGIN_URL, json=payload, headers=headers)
        assert (response.status_code == 404 and
                response.json() == {'code': 404, 'message': 'Учетная запись не найдена'})
