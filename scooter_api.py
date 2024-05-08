import allure
import requests
from urls import Urls


class ScooterApi:
    @staticmethod
    @allure.step('Создание нового курьера')
    def create_courier(body):
        return requests.post(url=Urls.CREATE_OR_DELETE_COURIER, json=body)

    @staticmethod
    @allure.step('Логин курьера в системе')
    def login_courier(body):
        return requests.post(url=Urls.LOGIN_COURIER, json=body)

    @staticmethod
    @allure.step('Удаление курьера с помощью тела ответа логина курьера в системе')
    def delete_courier(body_login_courier, return_response):
        response = ScooterApi.login_courier(body=body_login_courier)
        if return_response:
            return requests.delete(url=Urls.DELETE_COURIER + str(response.json()["id"]))
        else:
            requests.delete(url=Urls.DELETE_COURIER + str(response.json()["id"]))

    @staticmethod
    @allure.step('Удаление курьера по id')
    def delete_courier_on_id(courier_id, return_request):
        if return_request:
            return requests.delete(url=Urls.DELETE_COURIER + str(courier_id))
        else:
            requests.delete(url=Urls.DELETE_COURIER + str(courier_id))

    @staticmethod
    @allure.step('Создание заказа')
    def create_order(body):
        return requests.post(url=Urls.CREATE_OR_GET_ORDERS, json=body)

    @staticmethod
    @allure.step('Отменить заказ')
    def cancel_order(track_order):
        return requests.put(url=Urls.CANCEL_ORDER + f'?track={track_order}')

    @staticmethod
    @allure.step('Получение списка заказов')
    def get_order_list():
        return requests.get(url=Urls.CREATE_OR_GET_ORDERS)

    @staticmethod
    @allure.step('Получение заказа по его номеру')
    def get_order_on_number(number=None):
        if number:
            return requests.get(url=Urls.GET_ORDER_TRACK_ON_NUMBER + str(number))
        else:
            return requests.get(url=Urls.GET_ORDER_TRACK_ON_NUMBER)

    @staticmethod
    @allure.step('Принять заказ')
    def accept_order(order_id, courier_id):
        return requests.put(url=Urls.ACCEPT_ORDER + str(order_id) + "?courierId=" + str(courier_id))
