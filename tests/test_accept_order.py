import allure
import pytest

from courier_registration import CourierRegistration
from data import Data
from helper import Helper
from scooter_api import ScooterApi


class TestAcceptOrder:
    @allure.title('Позитивный тест принятия заказа.')
    @allure.description('Создание заказа и курьера и принятие заказа. Ожидаем 200 статус код и успешный ответ')
    def test_accept_order_result_order_accept(self):
        # Создаем курьера и логинимся под ним, для получения ID
        create_courier = CourierRegistration.register_new_courier_and_return_login_password_or_return_random_payload("")
        body_from_login = Helper.modify_login_courier(create_courier[:2])
        login_courier = ScooterApi.login_courier(body_from_login)
        courier_id = login_courier.json()["id"]

        # Создаем заказ и выполняем поиск заказа и забираем его id
        create_order = ScooterApi.create_order(body=Data.CREATE_ORDER)
        order_track = create_order.json()["track"]

        get_number_order = ScooterApi.get_order_on_number(order_track)
        order_id = get_number_order.json()["order"]["id"]

        # Передаем необходимые данные для принятия номера заказа
        accept_order = ScooterApi.accept_order(order_id=order_id, courier_id=courier_id)

        assert accept_order.status_code == 200 and \
               accept_order.json()["ok"] is True

        # Удаляем курьера и отменяем заказ в конце теста
        ScooterApi.delete_courier_on_id(courier_id=login_courier.json()["id"], return_request=False)
        ScooterApi.cancel_order(create_order.json()["track"])

    @allure.title('Негативный тест принятия заказа. Курьра с ID не существуют')
    @allure.description('Создание заказ и курьера(сразу удаление) и принятие заказа. '
                        'Ожидаем 404 статус код и ошибка в теле ответа')
    def test_accept_order_deleted_courier_id_failed_accept_order(self):
        # Создаем курьера и удаляем, берем ID удаленного курьера
        create_courier = CourierRegistration.register_new_courier_and_return_login_password_or_return_random_payload("")
        body_from_login = Helper.modify_login_courier(create_courier[:2])
        login_courier = ScooterApi.login_courier(body_from_login)
        courier_id = login_courier.json()["id"]
        ScooterApi.delete_courier_on_id(courier_id=login_courier.json()["id"], return_request=False)

        # Создаем заказ и выполняем поиск заказа и забираем его id
        create_order = ScooterApi.create_order(body=Data.CREATE_ORDER)
        order_track = create_order.json()["track"]
        get_number_order = ScooterApi.get_order_on_number(order_track)
        order_id = get_number_order.json()["order"]["id"]

        # Передаем необходимые данные для принятия номера заказа
        accept_order = ScooterApi.accept_order(order_id=order_id, courier_id=courier_id)

        assert accept_order.status_code == 404 and \
               accept_order.json()["message"] == 'Курьера с таким id не существует'

        # Отменяем заказ в конце теста
        ScooterApi.cancel_order(create_order.json()["track"])

    @allure.title('Негативный тест принятия заказа. Заказа с указанным ID не существует')
    @allure.description('Создание курьера и принятие заказа по несуществующему ID заказа. '
                        'Ожидаем 404 статус код и ошибка в теле ответа')
    def test_accept_order_random_order_id_failed_accept_order(self):
        # Создаем курьера и берем его ID
        create_courier = CourierRegistration.register_new_courier_and_return_login_password_or_return_random_payload("")
        body_from_login = Helper.modify_login_courier(create_courier[:2])
        login_courier = ScooterApi.login_courier(body_from_login)
        courier_id = login_courier.json()["id"]

        # Подставляем рандомное значение в переменную ID заказа
        order_id = Helper.random_number_from_tests()

        # Передаем необходимые данные для принятия номера заказа
        accept_order = ScooterApi.accept_order(order_id=order_id, courier_id=courier_id)

        assert accept_order.status_code == 404 and \
               accept_order.json()["message"] == 'Заказа с таким id не существует'

        # Удаляем курьера
        ScooterApi.delete_courier_on_id(courier_id=login_courier.json()["id"], return_request=False)

    @allure.title('Негативный тест принятия заказа. Не передаем ID курьера')
    @allure.description('Передаем пустое значение ID курьера. Ожидаем 400 статус код и ошибку в теле ответа')
    def test_accept_order_empty_courier_id_failed_accept_order(self):
        # Передаем необходимые данные для принятия заказа
        accept_order = ScooterApi.accept_order(order_id=Helper.random_number_from_tests, courier_id="")

        assert accept_order.status_code == 400 and \
               accept_order.json()["message"] == 'Недостаточно данных для поиска'

    @allure.title('Негативный тест принятия заказа. Не передаем ID заказа')
    @allure.description('Передаем пустое значение ID заказа. Ожидаем 404 статус код и ошибку в теле ответа')
    def test_accept_order_empty_order_id_failed_accept_order(self):
        # Передаем необходимые данные для принятия заказа
        accept_order = ScooterApi.accept_order(order_id="", courier_id=Helper.random_number_from_tests)

        assert accept_order.status_code == 404 and \
               accept_order.json()["message"] == 'Not Found.'
