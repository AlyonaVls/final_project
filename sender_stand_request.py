import configuration
import requests
import data

# Запрос на создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)
# Запрос на получение заказа по треку заказа
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.TAKE_ORDER + 'track')

