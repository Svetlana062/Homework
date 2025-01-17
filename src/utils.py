import json


def read_file(path: str) -> list[dict]:
    """Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print("Ошибка при декодировании")
                return []
        return data
    except FileNotFoundError:
        print("Файл не найден")
        return []


print(read_file("./data/operations.json"))
