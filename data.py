class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    COURIER_CREATE_URL = BASE_URL + '/api/v1/courier'
    ORDERS_CREATE_URL = BASE_URL + '/api/v1/orders'
    COURIER_LOGIN_URL = BASE_URL + '/api/v1/courier/login'
    COURIER_DELETE_URL = BASE_URL + '/api/v1/courier'

login_valid = 'valkiriya'
password_valid = '3333333!'

order_black = {
    "firstName": "John",
    "lastName": "Snow",
    "address": "the Wall",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-08-06",
    "comment": "I don't know nothing",
    "color": [
        "BLACK"
    ]
}

order_grey = {
    "firstName": "Daenerys",
    "lastName": "Targaryen",
    "address": "Antient Valyria",
    "metroStation": 4,
    "phone": "+7 800 355 35 00",
    "rentTime": 5,
    "deliveryDate": "2024-08-06",
    "comment": "Drakaris",
    "color": [
        "GREY"
    ]
}

order_black_grey = {
    "firstName": "Tyrion",
    "lastName": "Lannister",
    "address": "Caterly Rock",
    "metroStation": 3,
    "phone": "+7 800 355 0988",
    "rentTime": 1,
    "deliveryDate": "2024-08-06",
    "comment": "I talk too much",
    "color": [
        "GREY", "BLACK"
    ]
}

order_no_color = {
    "firstName": "Sansa",
    "lastName": "Stark",
    "address": "Winterfell",
    "metroStation": 3,
    "phone": "+7 800 445 0988",
    "rentTime": 4,
    "deliveryDate": "2024-08-06",
    "comment": "I like dogs",
    "color": []
}