import random


def generate_email():
    number = random.randint(1, 99999999)
    return f"test_{number}@mail.ru"
