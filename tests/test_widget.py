import pytest

from src.widget import get_date, mask_account_card


# Тест для проверки маскировки карт/счетов и универсальности функции
@pytest.mark.parametrize(
    "value, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


# Тесты на ошибочный ввод наименований и номеров карт/счетов
@pytest.mark.parametrize(
    "input_error",
    [
        "Maestro",
        "Visa Gold",
        "Счет",
        "MasterCard 6895859759",
        "Visa Platinum 6975975765864865486487646",
        "Счет 678698687",
        "Счет 35383033474447895560767856",
        "Некорректные данные",
    ],
)
def test_mask_account_card_error(input_error: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(input_error)


# Тесты на вывод корректной даты
@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2018-09-12T21:27:25.241689", "12.09.2018"),
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
    ],
)
def test_get_date(value: str, expected: str) -> None:
    assert get_date(value) == expected


# Тест на ошибочный ввод данных даты
@pytest.mark.parametrize(
    "input_error",
    ["31-02-2023", "2023/02/31", "31st of February, 2023", "2023-02", "02-2023", "дата: 31.02.2023", "31.02.23"],
)
def test_get_date_error(input_error: str) -> None:
    with pytest.raises(IndexError):
        get_date(input_error)
