from random import randint
import allure

from data import Data


class Helper:
    @staticmethod
    @allure.step('Редактирование тела запроса на создание заказа')
    def modify_create_order_data(key, value):
        body = Data.CREATE_ORDER.copy()
        body[key] = value

        return body

    @staticmethod
    @allure.step('Изменение стандартного тела запроса на логин курьера в системе')
    def modify_login_courier(array_courier_data):
        body = Data.LOGIN_COURIER.copy()
        body["login"] = array_courier_data[0]
        body["password"] = array_courier_data[1]

        return body

    @staticmethod
    @allure.step('Изменение стандартного тела запроса на создание курьера')
    def modify_create_default_courier(array_courier_body):
        body = Data.CREATE_COURIER_DEFAULT.copy()
        body["login"] = array_courier_body[0]
        body["password"] = array_courier_body[1]
        body["firstName"] = array_courier_body[2]

        return body

    @staticmethod
    @allure.step('Изменение ключа значения тела запроса.')
    def modify_body_request(body, key, value):
        body[key] = value

        return body

    @staticmethod
    @allure.step('Удаление поля firstName из объекта для регистрации')
    def delete_last_name_body(body_registration):
        del body_registration["firstName"]

        return body_registration

    @staticmethod
    @allure.step('Формируем случайное число')
    def random_number_from_tests():
        return randint(999999, 9999999)
