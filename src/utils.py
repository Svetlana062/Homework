import json
import logging
import pathlib

root_directory = pathlib.Path(__file__).parent.parent.resolve()

# Формируем абсолютный путь к файлу логов
log_path = root_directory / "logs" / "utils.log"

logger = logging.getLogger("utils")  # логер с именем текущего модуля
file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
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
        return list(data)
    except FileNotFoundError:
        logger.error(f"Файл {path} не найден.")
        return []
