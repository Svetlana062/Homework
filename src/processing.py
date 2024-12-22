def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и опционально значение для
    ключа state (по умолчанию 'EXECUTED'). Функция возвращает новый
    список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    new_list = []
    for dictionary in list_of_dicts:
        if dictionary.get("state") == state:
            new_list.append(dictionary)
    return new_list


def sort_by_date(list_of_dicts: list, reverse: bool = True) -> list:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция должна
    возвращать новый список, отсортированный по дате (date). Выход функции
    (сортировка по убыванию, то есть сначала самые последние операции)."""
    new_sorted_list = sorted(list_of_dicts, key=lambda x: x["date"], reverse=True)
    return new_sorted_list
