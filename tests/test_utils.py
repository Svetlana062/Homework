import json

import pytest

from src.utils import get_operators_info


@pytest.fixture
def valid_json_file(tmp_path):
    """Создает временный файл с валидным JSON для теста."""
    data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
    file_path = tmp_path / "test_utils.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return str(file_path)


def test_get_operators_info(valid_json_file):
    """Тест на то, принимает ли функция на вход путь до JSON-файла
    и возвращает ли список словарей с данными о финансовых транзакциях."""
    expected = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
    result = get_operators_info(valid_json_file)
    assert result == expected


def test_get_operators_info_no_file():
    """Тест на случай, когда файл не существует."""
    result = get_operators_info("./data/non_existent_file.json")
    assert result == []
