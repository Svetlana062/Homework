import unittest
from unittest.mock import patch

from src.reading_files import read_transactions_from_csv, read_transactions_from_excel


@patch("pandas.read_csv")
def test_read_transactions_from_csv(mock_read_file):
    """Тесты для функции считывания финансовых операций из CSV-файлов."""
    mock_read_file.return_value.to_dict.return_value = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    result = read_transactions_from_csv("transactions.csv")
    assert result == [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]


class TestFinancialOperations(unittest.TestCase):

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel(self, mock_read_excel):
        """Тесты для функции считывания финансовых операций из Excel-файлов."""
        mock_read_excel.return_value.to_dict.return_value = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]

        expected = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
        result = read_transactions_from_excel("test_transactions.xlsx")
        self.assertEqual(result, expected)


def test_transactions_csv_empty_filename():
    """Проверяет, что функция возвращает пустой список, если имя файла пустое."""
    assert read_transactions_from_csv("") == []


def test_read_csv_invalid_path():
    """Проверяет, что функция возвращает пустой список, если в качестве аргумента
    передан некорректный путь"""
    transactions = read_transactions_from_csv("some/invalid/path")
    assert transactions == []
