import allure
import pytest

from data import Data
from helper import Helper
from scooter_api import ScooterApi


class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа')
    @allure.description('Создание заказа с разными цветами')
    @pytest.mark.parametrize('key, value', Data.COLOR_FROM_CREATE_ORDER)
    def test_create_order_success_registration(self, key, value):
        create_order = ScooterApi.create_order(body=Helper.modify_create_order_data(key, value))

        assert create_order.status_code == 201 and \
               "track" in create_order.json()

        ScooterApi.cancel_order(create_order.json()["track"])
