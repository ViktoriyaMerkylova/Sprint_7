class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    COURIER_CREATE_URL = BASE_URL + '/api/v1/courier'
    ORDERS_CREATE_URL = BASE_URL + '/api/v1/orders'
    COURIER_LOGIN_URL = BASE_URL + '/api/v1/courier/login'
    COURIER_DELETE_URL = BASE_URL + '/api/v1/courier'

login_valid = 'valkiriya'
password_valid = '3333333!'

order_black = {
    "firstName": "Vika",
    "lastName": "Merkulova",
    "address": "United States of America",
    "metroStation": 4,
    "phone": "+7 999 720 50 46",
    "rentTime": 5,
    "deliveryDate": "2025-04-04",
    "comment": "I don't know nothing",
    "color": [
        "BLACK"
    ]
}

order_grey = {
    "firstName": "Clarence",
    "lastName": "Endicott",
    "address": "Kaitlin Bentley",
    "metroStation": 4,
    "phone": "+7 998 721 51 47",
    "rentTime": 5,
    "deliveryDate": "2025-03-03",
    "comment": "Stacey",
    "color": [
        "GREY"
    ]
}

order_black_grey = {
    "firstName": "Faithe",
    "lastName": "Easton",
    "address": "Cassy Traylor",
    "metroStation": 3,
    "phone": "+7 997 355 52 48",
    "rentTime": 1,
    "deliveryDate": "205-03-01",
    "comment": "Addilyn Appleton",
    "color": [
        "GREY", "BLACK"
    ]
}

order_no_color = {
    "firstName": "Hardy",
    "lastName": "Davids",
    "address": "Finley Bentley",
    "metroStation": 3,
    "phone": "+7 888 545 12 34",
    "rentTime": 4,
    "deliveryDate": "2025-01-01",
    "comment": "Mo Silver",
    "color": []
}