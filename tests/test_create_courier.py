import allure
import pytest

from data import Data
from scooter_api import ScooterApi
from courier_registration import CourierRegistration
from helper import Helper


class TestCreateCourier:
    @allure.title('Позитивный кейс создания курьера')
    @allure.description('Создание курьера с помощью рандомных данных. '
                        'Ожидаем статус код 201 и сообщение об успешной регистрации')
    def test_create_courier_success_create_and_ok_true(self):
        body = CourierRegistration.register_new_courier_and_return_login_password_or_return_random_payload("random_data")
        create_courier = ScooterApi.create_courier(body=body)

        assert create_courier.status_code == 201 and \
               create_courier.json()["ok"] is True
        # Удаление курьера
        ScooterApi.delete_courier(Helper.delete_last_name_body(body), False)

    @allure.title('Негативный кейс создания курьера, который уже зарегистрирован')
    @allure.description('Создание уже существующего курьера. Ожидаем стату 409 и сообщение с ошибкой')
    def test_create_two_identical_courier_status_code_error(self):
        body = CourierRegistration.register_new_courier_and_return_login_password_or_return_random_payload("")
        body_modify = Helper.modify_create_default_courier(body)
        create_courier = ScooterApi.create_courier(body=body_modify)

        assert create_courier.status_code == 409 and \
               create_courier.json()["message"] == "Этот логин уже используется. Попробуйте другой."
        # Удаление курьера
        ScooterApi.delete_courier(Helper.delete_last_name_body(body_modify), False)

    @allure.title('Негативный тест создания курьера, когда обязательные поля не заполнены')
    @allure.description('Создание курьера, обязательные поля - пустые. Ожидаем статус 400 и сообщение об ошибке')
    @pytest.mark.parametrize('key', Data.KEY_FROM_LOGIN_AND_CREATE_COURIER_TEST)
    def test_create_courier_required_field_is_empty_status_code_error(self, key):
        body = CourierRegistration.register_new_courier_and_return_login_password_or_return_random_payload(
            "random_data")
        body_modify = Helper.modify_body_request(body=body, key=key, value="")
        create_courier = ScooterApi.create_courier(body=body_modify)

        assert create_courier.status_code == 400 and \
               create_courier.json()["message"] == "Недостаточно данных для создания учетной записи"

