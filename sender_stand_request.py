import configuration
import requests
import data

# Запрос на создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)
response = post_new_order(data.body_order)
# Сохранение номера трека заказа в переменной
result = response.json()['track']

# Запрос на получение заказа по треку заказа
def get_order():
    return requests.get(configuration.URL_SERVICE + configuration.TAKE_ORDER + 'result')
response = get_order()

