import random
import time
from logic.Auth_Service import AuthService

class PaymentService:
    def __init__(self):
        self.warehouse = {"КоробкаЕды": {"Цена": 500, "Статус": "Не оплачен"}, "Еда": {"Цена": 100, "Статус": "Не оплачен"}} # Словарь, где мы будем обрабатывать платежи. Там товары которые мы покупаем.
    
    def purchase(self, balance, Authservice):
        name = input(f"Введите название товара из существующих: {self.warehouse}\n >>>")
        if name in self.warehouse and self.warehouse[name]["Цена"] <= balance:
            if Authservice.authorized_user != "":
                print(f"Вы купили {name} на сумму {self.warehouse[name]['Цена']}₽")
                balance -= self.warehouse[name]["Цена"]
                print("Поиск курьера...")
                while True:
                    r1 = random.randint(1, 5)
                    time.sleep(2)
                    if r1 == 1:
                        self.warehouse[name]["Статус"] = "Оплачено, курьер найден, ожидайте доставки."
                        print(self.warehouse[name]["Статус"])
                        break
                
        else:
            print("Такого товара нет, или же не хватает денег на счету.")
            
            
            
            

    