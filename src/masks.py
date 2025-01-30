import logging
import pathlib
from logging import FileHandler

root_directory = pathlib.Path(__file__).parent.parent.resolve()

# Формируем абсолютный путь к файлу логов
log_path = root_directory / "logs" / "masks.log"

logger = logging.getLogger("masks")  # логер с именем текущего модуля
file_handler: FileHandler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

logger.debug("Debug message")


def get_mask_card_number(card_number: str) -> str:
    """Маскируем и разбиваем номер карты с помощью f-строки и срезов"""
    try:
        card_number_list = card_number.split()
        card_number_without_space = "".join(card_number_list)
        if card_number_without_space.isdigit() is True and len(card_number_without_space) == 16:
            masked_card_number = (
                f"{card_number_without_space[:4]} {card_number_without_space[4:6]}** "
                f"**** {card_number_without_space[12:]}"
            )
            logger.info("Маскировка номера карты: %s", masked_card_number)
            return masked_card_number

        elif card_number_without_space.isdigit() is False or len(card_number_without_space) != 16:
            logger.error("Некорректный номер карты: %s", card_number)
            raise ValueError("Вы ввели некорректные данные")

    except Exception as e:
        logger.exception("Ошибка в функции get_mask_card_number: %s", e)
        raise


def get_mask_account(number: str) -> str:
    """Принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX"""
    try:
        if number.isdigit() is False or len(number) != 20:
            logger.error("Некорректный номер счета: %s", number)
            raise ValueError("Вы ввели некорректные данные")
        masked_account_number = f"**{number[-4:]}"
        logger.info("Маскировка номера счета: %s", masked_account_number)
        return masked_account_number
    except Exception as e:
        logger.exception("Ошибка в функции get_mask_account: %s", e)
        raise
