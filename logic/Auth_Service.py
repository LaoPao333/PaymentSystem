from errors.password_error import password_processing
from errors.name_error import name_processing
from errors.error_name_password import name_password_error
class AuthService:
    def __init__(self):
        self.user_storage = {}
        self.authorized_user = ""
    
    def registration(self):
        name = input("Введите ваше имя: ")
        password = input("Введите ваш пароль: ")
        if password == "" or name == "":
            return
        name = name_processing(name)
        password = password_processing(password)
        next = name_password_error(name, password)
        if next == True:
            self.user_storage[name] = {"Пароль": password}
            print(self.user_storage)
            
    def autorization(self): 
        name = input("Введите ваше имя: ")
        password = input("Введите ваш пароль: ")
        if password == "" or name == "":
            return
        
        elif name in self.user_storage and self.user_storage[name]["Пароль"] == password:
            self.authorized_user = name
            print(f"Вы успешно вошли! {self.authorized_user}")
        else:
            print("Неправильный логин или пороль!")

        
