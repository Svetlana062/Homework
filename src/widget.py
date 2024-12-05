from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: Union[str]) -> None | str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    split_input = user_input.split()
    if len(split_input) == 2:
        if split_input[0].lower() == "счет":
            new_input = "".join(split_input[-1])
            return f"{split_input[0]} {get_mask_account(new_input)}"
        else:
            new_input = "".join(split_input[-1])
            return f"{split_input[0]} {get_mask_card_number(new_input)}"
    elif len(split_input) == 3:
        new_input = "".join(split_input[-1])
        return f"{split_input[0]} {split_input[1]} {get_mask_card_number(new_input)}"
    else:
        return "Вы ввели некорректные данные"


def get_date(user_date: Union[str]) -> None | str:
    """Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")"""
    new_date = user_date.split("T")
    date = new_date[0].split("-")
    return f"{date[-1]}.{date[-2]}.{date[-3]}"
