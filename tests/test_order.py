import allure
import requests
from data import Url, Flags


class TestGetOrders:

    @allure.title('Проверка успешного получения списка заказов')
    @allure.description('Проверка получения кода 200 Ok и списка заказов с id заказа при отправке GET-запроса '
                        'на получение списка заказов')
    def test_get_orders_list_success(self):
        response = requests.get(f'{Url.ORDERS_CREATE_URL}')
        assert response.status_code == 200 and Flags.SUCCESSFUL_GET_ORDER_LIST in response.json()