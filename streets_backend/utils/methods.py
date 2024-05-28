from random import randint


def get_confirmation_code():
    """Получение секретного кода регистрации"""
    return randint(100000000, 999999999)
