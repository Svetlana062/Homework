from unittest.mock import patch

import pytest

from src.external_api import conversion_currency


@pytest.mark.parametrize(
    "in_data, received_data, expected",
    [
        (
            {
                "id": 214024827,
                "state": "EXECUTED",
                "date": "2018-12-20T16:43:26.929246",
                "operationAmount": {
                  "amount": "70946.18",
                  "currency": {
                    "name": "USD",
                    "code": "USD"
                  }
                },
                "description": "Перевод организации",
                "from": "Счет 10848359769870775355",
                "to": "Счет 21969751544412966366"
              },
            {
                'success': True,
                'query': {'from': 'USD', 'to': 'RUB', 'amount': 70946.18},
                'info': {'timestamp': 1737143224, 'rate': 102.500487},
                'date': '2025-01-17',
                'result': 7272018.00079
            },
            7272018.00079
        )
    ]
)
def test_conversion_currency(in_data: dict, received_data: dict, expected: float) -> None:
    #Тест на конвертацию валюты с помощью обращения к внешнему API для получения текущего курса валют
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = received_data
        assert conversion_currency(in_data) == expected
