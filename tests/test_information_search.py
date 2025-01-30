import unittest
from collections import Counter

from src.information_search import count_category_of_transactions, find_description


class TestTransactionFunctions(unittest.TestCase):

    def setUp(self):
        """Создаем тестовые данные"""
        self.transactions = [
            {"id": 1, "description": "Перевод на счет", "state": "EXECUTED"},
            {"id": 2, "description": "Перевод с карты", "state": "EXECUTED"},
            {"id": 3, "description": "Оплата счета", "state": "CANCELED"},
            {"id": 4, "description": "Возврат средств", "state": "EXECUTED"},
            {"id": 5, "description": "Перевод с карты на счет", "state": "EXECUTED"},
        ]

    def test_find_description_case_insensitive(self):
        """Тест для функции на нечувствительность к регистру."""
        result = find_description(self.transactions, "перевод")
        self.assertEqual(len(result), 3)  # Ожидаем, что найдем 3 транзакции
        self.assertIn(self.transactions[0], result)
        self.assertIn(self.transactions[1], result)
        self.assertIn(self.transactions[4], result)

    def test_find_description_not_found(self):
        """Тест для функции, когда ни одна запись не найдена."""
        result = find_description(self.transactions, "несуществующий запрос")
        self.assertEqual(result, [])  # Ожидаем пустой список

    def test_count_category_of_transactions(self):
        """Тест для функции."""
        categories = ["Перевод на счет", "Оплата счета", "Возврат средств"]
        result = count_category_of_transactions(self.transactions, categories)
        expected_result = Counter({"Перевод на счет": 1, "Оплата счета": 1, "Возврат средств": 1})
        self.assertEqual(result, expected_result)

    def test_count_category_of_transactions_no_matches(self):
        """Тест для функции, когда совпадений нет."""
        categories = ["Перевод на счет", "Некорректная категория"]
        result = count_category_of_transactions(self.transactions, categories)
        expected_result = Counter({"Перевод на счет": 1})  # Ожидаем 1 для "Перевод на счет"
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
