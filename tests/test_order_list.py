import allure

from scooter_api import ScooterApi


class TestOrderList:
    @allure.title('Проверка получения списка всех заказов')
    @allure.description('Проверка status_code == 200 и что json пришёл не пустой')
    def test_get_order_list_order_list_is_not_none(self):
        order_list = ScooterApi.get_order_list()

        assert order_list.status_code == 200 and \
               order_list.json()["orders"] is not None
