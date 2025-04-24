import allure
import pytest
import requests
from helpers import generate_random_string
from data import Url, password_valid, login_valid, ResponseBody


class TestCreateLogin:
    @allure.title('Проверка возможности авторизации курьера и необходимости передачи всех обязательных полей, успешный запрос возвращает id')
    @allure.description('Проверка получения кода 200 Ok и сообщения {"id": [___]} при отправке POST-запроса '
                        'на авторизацию курьера при заполненных полях login и password валидными данными')
    def test_login_courier(self, create_courier):
        response = requests.post(f'{Url.COURIER_LOGIN_URL}', json=create_courier[1])
        courier_id = response.json()
        assert response.status_code == 200 and courier_id != ''

    @allure.title('Проверка ошибки, если неправильно указать логи или пароль/авторизоваться под несуществующим пользователем')
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
        assert response.status_code == 404 and (response.json() == ResponseBody.COURIER_ACCOUNT_NOT_FOUND)



    @allure.title('Проверка неудачного логина курьера при отсутсвии заполненного login/password')
    @allure.description('Проверка получения кода 400 Bad request и сообщения '
                        '{"message": "Недостаточно данных для входа"} при отправке POST-запроса '
                        'на авторизацию курьера при незаполненных полях login/password')
    @pytest.mark.parametrize('login, password', [
        ('', generate_random_string(10)),
        (generate_random_string(10), '')
    ])
    def test_login_courier_without_required_fields_failed(self, login, password):
        payload = {'login': login, 'password': password}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Url.COURIER_LOGIN_URL, json=payload, headers=headers)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_LOGIN_NOT_ENOUGH_DATA)