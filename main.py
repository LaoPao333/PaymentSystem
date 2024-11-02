from logic.Auth_Service import AuthService
from logic.Payment_Service import PaymentService
from logic.Order_Service import create_order


Authservice = AuthService()
Paymentservice = PaymentService()

balance = 1000 # Баланс на счету, можете поменять что бы увеличить свой баланс.


while True:
    user_input = input("1: Регистрация\n2: Авторизация\n3: Выбор/Оплата товара\n4: Проверка статуса платежа\n5: Создать свой заказ"
                       "\n-- >")
    if user_input == "1":
        Authservice.registration()
    elif user_input == "2":
        Authservice.autorization()
    elif user_input == "3":
        Paymentservice.purchase(balance, Authservice)
    elif user_input == "4":
        Paymentservice.status_of_purchase()
    elif user_input == "5":
        create_order(Paymentservice)
    else:
        print("Такого нет")

