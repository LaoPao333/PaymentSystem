def name_processing(name):
    errors = []
    while True:
        if len(name) < 3:
            errors.append("Имя должно содержать не менее 3 символов!")
        if not errors:
            break
        if errors:
            print("------------ \n".join(errors))
            break
    words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 
        'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    rus_letters = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", 
                   "И", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", 
                   "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я",
               "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "к", 
               "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    
    name_list = []
    name_string = ''
    name_warning = False
    for i in name:
        if i in rus_letters:
            print("Имя не должно содержать русских букв!")
            break
        elif i in words:
            name_list.append(i)
        else:
            name_warning = True
            pass
    for i in name_list:
        name_string += i  
    if name_warning == True:
        print(f"----------------\nВаше имя было обработано: {name_string}\n----------------")
    name = name_string
    return name
   
        
            
