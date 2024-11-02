import random
from logic.Payment_Service import PaymentService


def create_order(Paymentservice):
    r1 = random.randint(100, 10000)
    name = input("Введите название того товара, что вы хотите купить: ")
    if name in Paymentservice.warehouse:
        print("Такой заказ уже существует!")
    else:
        Paymentservice.warehouse[name] = {"Цена": r1, "Статус": "Не оплачен"}
        print("Заказ был создан! Пожалуйста оплатите его , и ожидайте доставки! :)")
        print(Paymentservice.warehouse)