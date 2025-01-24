import json
import logging

logger = logging.getLogger("utils")  # логер с именем текущего модуля
file_handler = logging.FileHandler("../logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

logger.debug("Debug message")


def get_operators_info(path: str) -> list[dict]:
    """Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                logger.info(f"Файл {path} успешно загружен.")
            except json.JSONDecodeError:
                logger.error(f"Ошибка при декодировании JSON-файла {path}.")
                return []
        return data
    except FileNotFoundError:
        logger.error(f"Файл {path} не найден.")
        return []


print(get_operators_info("../data/operations.json"))
