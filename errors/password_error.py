
def password_processing(password):
    errors = [""]
    while True:
        if len(password) < 4:
            errors.append("Пароль должен содержать не менее 4 символов!")
        if not errors:
            break
        if errors:
            print("----------------\n".join(errors))
            break

    
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    
    words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 
            'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    

    word = []
    password_string = ''
    password_warning = False
    for i in password:
        if i in numbers:
            word.append(i)
        elif i in words:
            word.append(i)
        else:
            password_warning = True
            pass        
    for i in word:
        password_string += i
        
    if password_warning == True:
        print(f"--------------\nВаш пороль был обработан: {password_string}\n--------------")


    password = password_string
    return password
        
            



 
