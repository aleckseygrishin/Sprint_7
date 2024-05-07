import allure
import requests
import data
from urls import Urls


class ScooterApi:
    @staticmethod
    @allure.step('Логин курьера в системе')
    def login_courier(body):
        return requests.post(url=Urls.LOGIN_COURIER, json=body)

    @staticmethod
    @allure.step('Удаление курьера')
    def delete_courier(courier_id):
        return requests.delete(url=Urls.DELETE_COURIER + courier_id)
