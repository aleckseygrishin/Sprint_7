class Data:
    CREATE_ORDER = {
        "firstName": "Ar",
        "lastName": "Har",
        "address": "Honoha, 142 apt.",
        "metroStation": 5,
        "phone": "+7 800 555 35 35",
        "rentTime": 4,
        "deliveryDate": "2024-05-08",
        "comment": "Saske, come back to Honoha",
        "color": [
            "BLACK"
        ]
    }

    LOGIN_COURIER = {
        "login": "ninja",
        "password": "1234"
    }

    CREATE_COURIER_DEFAULT = {
        "login": "ninja",
        "password": "1234",
        "firstName": "bibi"
    }

    COLOR_FROM_CREATE_ORDER = [
        ["color", ["BLACK"]],
        ["color", ["GREY"]],
        ["color", []],
        ["color", ["BLACK", "GREY"]]
    ]

    KEY_FROM_LOGIN_AND_CREATE_COURIER_TEST = [
        "login",
        "password"
    ]
