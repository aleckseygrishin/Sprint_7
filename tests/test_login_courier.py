import allure
import pytest

from courier_registration import CourierRegistration
from data import Data
from helper import Helper
from scooter_api import ScooterApi


class TestLoginCourier:
    @allure.title('Позитивный тест авторизации курьера.')
    @allure.description('Регистрация и авторизацию курьера. Ожидаем 200 статус код и положительный ответ в теле')
    def test_success_auth_courier_status_code_and_message_positive(self):
        create_courier = CourierRegistration.register_new_courier_and_return_login_password_or_return_random_payload("")
        body_from_login = Helper.modify_login_courier(create_courier[:2])
        login_courier = ScooterApi.login_courier(body_from_login)

        assert login_courier.status_code == 200 and login_courier.json()["id"] is not None

        # Удаление курьера по ID
        ScooterApi.delete_courier_on_id(courier_id=login_courier.json()["id"], return_request=False)

    @allure.title('Негативный тест авторизации курьера. Поля для авторизации - пустые')
    @allure.description('Авторизацию курьера без заполнения полей. Ожидаем 400 статус код и ошибку в теле ответа')
    @pytest.mark.parametrize('key', Data.KEY_FROM_LOGIN_AND_CREATE_COURIER_TEST)
    def test_failed_auth_courier_empty_field_status_code_and_message_error(self, key):
        body_to_req_login_courier_with_field_last_name = \
            CourierRegistration.register_new_courier_and_return_login_password_or_return_random_payload("random_data")
        body_to_req = Helper.delete_last_name_body(body_to_req_login_courier_with_field_last_name)
        body = Helper.modify_body_request(body=body_to_req, key=key, value="")
        login_courier = ScooterApi.login_courier(body)

        assert login_courier.status_code == 400 and login_courier.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Негативный тест авторизации незарегистрированного курьера.')
    @allure.description('Авторизацию незарегистрированного курьера. Ожидаем 404 статус код и ошибку в теле ответа')
    def test_failed_auth_courier_not_registration_courier_status_code_and_message_error(self):
        body_to_req_login_courier_with_field_last_name = \
            CourierRegistration.register_new_courier_and_return_login_password_or_return_random_payload("random_data")
        body_to_req = Helper.delete_last_name_body(body_to_req_login_courier_with_field_last_name)
        login_courier = ScooterApi.login_courier(body_to_req)

        assert login_courier.status_code == 404 and login_courier.json()["message"] == "Учетная запись не найдена"
