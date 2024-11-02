def name_password_error(name, password):
    if not name.isalpha() or not password.isdigit() or len(password) < 4 or len(name) < 3:
        return False
    else:
        return True
        