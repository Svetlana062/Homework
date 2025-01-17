import pytest

from src.utils import read_file


@pytest.mark.parametrize(
    "path_file, expected",
    [
        (
            "./data/test_utils.json",
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                }
            ],
        )
    ],
)
def test_read_file(path_file: str, expected: list) -> None:
    result = read_file(path_file)
    assert result == expected
