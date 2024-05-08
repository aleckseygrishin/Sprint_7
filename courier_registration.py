import random
import string
import allure

from scooter_api import ScooterApi


class CourierRegistration:
    # метод регистрации нового курьера возвращает список из логина и пароля
    # если регистрация не удалась, возвращает пустой список
    @staticmethod
    @allure.step('Создаем рандомные данные для регистрации курьера')
    def register_new_courier_and_return_login_password_or_return_random_payload(registration_or_random_data):
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # Если нужны рандомные данные для регистрации пользователя, то возвращаем их в ввиде объекта
        if registration_or_random_data == "random_data":
            return payload

        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = ScooterApi.create_courier(payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
        return login_pass
