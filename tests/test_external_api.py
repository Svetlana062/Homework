from unittest.mock import patch

import pytest

from src.external_api import conversion_currency


@pytest.mark.parametrize(
    "in_data, received_data, expected",
    [
        (
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "success": True,
                "query": {"from": "USD", "to": "RUB", "amount": 9824.07},
                "info": {"timestamp": 1737141077, "rate": 102.494979},
                "date": "2025-01-17",
                "result": 1006917.848345,
            },
            1006917.848345,
        )
    ],
)
def test_conversion_currency(in_data: dict, received_data: dict, expected: float) -> None:
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = received_data
        assert conversion_currency(in_data) == expected
