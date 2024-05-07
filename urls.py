class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_OR_DELETE_COURIER = f'{BASE_URL}/api/v1/courier'
    LOGIN_COURIER = f'{BASE_URL}/api/v1/courier/login'
    DELETE_COURIER = f'{BASE_URL}/api/v1/courier/'

    CREATE_OR_GET_ORDERS = f'{BASE_URL}/api/v1/orders'
    ACCEPT_ORDER = f'{BASE_URL}/api/v1/orders/accept/'
    GET_ORDER_TRACK = f'{BASE_URL}/api/v1/orders/track'