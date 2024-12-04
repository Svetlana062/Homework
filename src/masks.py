def get_mask_card_number(number: str) -> str:
    """Принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX"""
    new_string = f"{number[0:4]} {number[4:6]}** **** {number[12:]}"
    return new_string


def get_mask_account(number: str) -> str:
    """Принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX"""
    new_string = f"**{number[-4:]}"
    return new_string
