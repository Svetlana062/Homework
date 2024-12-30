from collections.abc import Iterator


def filter_by_currency(transactions_list: list[dict], currency_code: str = "USD") -> Iterator[dict]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    if not transactions_list:
        return iter([])
    if currency_code not in ["USD"]:
        return iter([])
    for transaction_ in transactions_list:
        if transaction_["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction_


def transaction_descriptions(my_list: list[dict]) -> Iterator[str]:
    """Напишите генератор transaction_descriptions, который принимает список
    словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction_ in my_list:
        yield transaction_["description"]


def card_number_generator(start, end):
    """
    Генератор, который выдает номера банковских карт. Генератор может сгенерировать номера карт в заданном
    диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.
    """
    for number in range(start, end + 1):
        if len(str(number)) < 16:
            card_number_not_formatted = "0" * (16 - len(str(number))) + str(number)
            number_card = f"{card_number_not_formatted[:4]} {card_number_not_formatted[4:8]} {card_number_not_formatted[8:12]} {card_number_not_formatted[12:]}"
            yield number_card
