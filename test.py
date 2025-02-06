# Алена Власова, 26-ая когорта, Финальный проект - инженер по тестированию плюс
import sender_stand_request
import data

def test():
# создание заказа
    create = sender_stand_request.post_new_order(data.body_order)
    # Сохраняем трек-номер заказа
    order_track = create.json()['track']
    # Получаем информацию о заказе по номеру трека
    response_get = sender_stand_request.get_order()
    # Проверяем, что код ответа равен 200
    assert response_get.status_code == 200