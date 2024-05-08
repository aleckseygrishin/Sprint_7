import allure

from data import Data
from helper import Helper
from scooter_api import ScooterApi


class TestGetOrderOnNumber:
    @allure.title('Позитивный тест получение заказа по его номеру')
    @allure.description('Создание и получение заказа по его номеру. '
                        'Ожидаем 200 статус код и track == track созданного заказа')
    def test_get_order_order_exist(self):
        create_order = ScooterApi.create_order(body=Data.CREATE_ORDER)
        order_number = create_order.json()["track"]

        check_order_on_number = ScooterApi.get_order_on_number(order_number)

        assert check_order_on_number.status_code == 200 and \
               check_order_on_number.json()["order"]["track"] == order_number

        ScooterApi.cancel_order(create_order.json()["track"])

    @allure.title('Негативный тест получение несуществующего заказа по его номеру')
    @allure.description('Получение несуществующего заказа по его номеру. '
                        'Ожидаем 404 статус код и сообщение об ошибке')
    def test_get_order_order_not_exist(self):
        random_order_number = Helper.random_number_from_tests()
        check_order_on_number = ScooterApi.get_order_on_number(random_order_number)

        assert check_order_on_number.status_code == 404 and \
               check_order_on_number.json()["message"] == "Заказ не найден"

    @allure.title('Негативный тест получение заказа без номера')
    @allure.description('Получение заказа без номера. '
                        'Ожидаем 400 статус код и сообщение об ошибке')
    def test_get_order_order_number_is_empty(self):
        check_order_on_number = ScooterApi.get_order_on_number()

        assert check_order_on_number.status_code == 400 and \
               check_order_on_number.json()["message"] == "Недостаточно данных для поиска"

