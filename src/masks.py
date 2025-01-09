

def get_mask_card_number(card_number: str) -> str:
    """Маскируем и разбиваем номер карты с помощью f-строки и срезов"""
    card_number_list = card_number.split()
    card_number_without_space = "".join(card_number_list)
    if card_number_without_space.isdigit() is False or len(card_number_without_space) != 16:
        raise ValueError("Вы ввели некорректные данные")
    masked_card_number = (f"{card_number_without_space[:4]} {card_number_without_space[4:6]}** " f"**** {card_number_without_space[12:]}")
    return masked_card_number


def get_mask_account(number: str) -> str:
    """Принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX"""
    if number.isdigit() is False or len(number) != 20:
        raise ValueError("Вы ввели некорректные данные")
    masked_account_number = f"**{number[-4:]}"
    return masked_account_number

