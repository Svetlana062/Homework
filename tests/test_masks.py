import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тесты на правильность маскировки номеров карт
@pytest.mark.parametrize(
    "value, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_get_mask_card_number(value: str, expected: str) -> None:
    assert get_mask_card_number(value) == expected


# Тесты на ошибочный ввод номеров карт
@pytest.mark.parametrize(
    "input_error",
    [
        "",
        "7865432678",
        "87654457899987666786877897",
        "Visa",
        "Visa Classic",
        "Некорректные данные"
    ]
)
def test_get_mask_card_number_error(input_error: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(input_error)




# Тесты на правильность маскировки номеров счетов
@pytest.mark.parametrize(
    "value, expected",
    [
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305")
    ],
)
def test_get_mask_account(value: str, expected: str) -> None:
    assert get_mask_account(value) == expected


# Тесты на ошибочный ввод номеров счетов
@pytest.mark.parametrize(
    "input_error",
    [
        "",
        "7865432678",
        "87654457899987666786877897",
        "Счет",
        "Некорректные данные",
        "Счет 876875875",
        "Счет 56865434678909876543212",
    ]
)
def test_mask_account_card_error(input_error: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(input_error)
