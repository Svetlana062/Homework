def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и опционально значение для
    ключа state (по умолчанию 'EXECUTED'). Функция возвращает новый
    список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    new_list = []
    for dictionary in list_of_dicts:
        if dictionary.get("state") == state:
            new_list.append(dictionary)
        elif dictionary.get("state") != state:
            continue
    return new_list


def sort_by_date(list_of_dicts: list[dict], revers: bool = True) -> list[dict]:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция должна
    возвращать новый список, отсортированный по дате (date)."""
    new_sorted_list = sorted(list_of_dicts, key=lambda x: x["date"], reverse=revers)
    return new_sorted_list
