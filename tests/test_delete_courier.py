import allure

from courier_registration import CourierRegistration
from helper import Helper
from scooter_api import ScooterApi


class TestDeleteCourier:
    @allure.title('Позитивный тест удаление созданного курьера.')
    @allure.description('Регистрация и удаление курьера. Ожидаем 200 статус код и положительный ответ в теле')
    def test_registration_and_delete_courier_success_delete_courier(self):
        create_courier = CourierRegistration.register_new_courier_and_return_login_password_or_return_random_payload("")
        body_from_login = Helper.modify_login_courier(create_courier[:2])
        login_courier = ScooterApi.login_courier(body_from_login)

        delete_courier = ScooterApi.delete_courier_on_id(courier_id=login_courier.json()["id"], return_request=True)

        assert delete_courier.status_code == 200 and delete_courier.json()["ok"] is True

    @allure.title('Негативный тест двойного удаление одного созданного курьера. ')
    @allure.description('Регистрация и двойное удаление курьера. Ожидаем 404 статус код и сообщение об ошибке в теле')
    def test_registration_and_double_delete_one_courier_delete_failed(self):
        create_courier = CourierRegistration.register_new_courier_and_return_login_password_or_return_random_payload("")
        body_from_login = Helper.modify_login_courier(create_courier[:2])
        login_courier = ScooterApi.login_courier(body_from_login)

        ScooterApi.delete_courier_on_id(courier_id=login_courier.json()["id"], return_request=False)
        delete_courier = ScooterApi.delete_courier_on_id(courier_id=login_courier.json()["id"], return_request=True)

        assert delete_courier.status_code == 404 and delete_courier.json()["message"] == 'Курьера с таким id нет.'

    @allure.title('Негативный тест удаление курьера без передачи ID.')
    @allure.description('Удаление курьера без передачи его ID. Ожидаем 404 статус код и сообщение об ошибке в теле')
    def test_delete_courier_with_empty_id_delete_failed(self):
        delete_courier = ScooterApi.delete_courier_on_id(courier_id="", return_request=True)

        assert delete_courier.status_code == 404 and delete_courier.json()["message"] == 'Not Found.'
