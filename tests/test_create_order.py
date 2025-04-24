import allure
import pytest
import requests
from data import Url, order_black, order_grey, order_black_grey, order_no_color


class TestCreateOrder:

    @allure.title('Проверка успешного создания заказа c BLACK,GREY, BLACK и GREY, без цвета. Тело ответа содержит track')
    @allure.description('Проверка получения кода 201 Created и сообщения {"ok": True} при отправке POST-запроса '
                        'на создание заказа при заполненном поле color одним цветом, двумя цветами и без цвета')
    @pytest.mark.parametrize('color', [order_black, order_grey, order_black_grey, order_no_color])
    def test_create_order_with_color_field_success(self, color):
        payload = color
        response = requests.post(Url.ORDERS_CREATE_URL, json=payload)
        assert response.status_code == 201 and 'track' in response.json()