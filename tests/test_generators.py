import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions, usd_transaction):
    """Функция тестирует выдачу списка операция по названию валют"""
    assert list(filter_by_currency(transactions, "USD")) == usd_transaction


@pytest.mark.parametrize("description", ["Перевод организации"])
def test_transaction_descriptions(transactions, description):
    """Функция тестирует выдачу списка описания операций"""
    trans = transaction_descriptions(transactions)
    assert next(trans) == description


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (5, 6, ["0000 0000 0000 0005", "0000 0000 0000 0006"]),
        (9, 10, ["0000 0000 0000 0009", "0000 0000 0000 0010"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: list[str]):
    """Функция тестирует генератор номеров карт"""
    generator = card_number_generator(start, stop)
    assert list(generator) == expected
