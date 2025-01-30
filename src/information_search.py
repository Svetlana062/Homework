import re
from collections import Counter


def find_description(list_of_dicts: list, find_str: str) -> list:
    """Поиск информации по описанию банковских операций"""
    list_of_description = []
    for entry in list_of_dicts:
        if re.search(find_str, entry["description"], re.IGNORECASE):
            list_of_description.append(entry)
    return list_of_description


def count_category_of_transactions(list_of_dicts: list, category_list: list) -> dict:
    """Подсчет встречающихся категорий операций из заданного списка"""
    list_transactions = []
    for some_dict in list_of_dicts:
        if some_dict["description"] in category_list:
            list_transactions.append(some_dict["description"])
    counted = Counter(list_transactions)
    return counted
