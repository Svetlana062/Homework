import os
import re

from src.generators import filter_by_currency
from src.information_search import find_description
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.reading_files import read_transactions_from_csv, read_transactions_from_excel
from src.utils import get_operators_info


def main():
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
    )

    while True:
        menu = int(input(":"))
        if menu == 1:
            print("Для обработки выбран JSON-файл.")
            path_to_file = os.path.join(os.path.dirname(__file__), "data", "operations.json")
            trans = get_operators_info(path_to_file)
            break

        elif menu == 2:
            print("Для обработки выбран CSV-файл.")
            path = os.path.join(os.path.dirname(__file__), "data", "transactions.csv")
            trans = read_transactions_from_csv(path)
            break

        elif menu == 3:
            print("Для обработки выбран XLSX-файл.")
            path = os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")
            trans = read_transactions_from_excel(path)
            break
        else:
            print("Неправильный выбор!")

    # Фильтрация по статусу
    print(
        """Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы:
    EXECUTED, CANCELED, PENDING"""
    )
    state = input(":")
    state = state.upper()
    while state != "EXECUTED" and state != "CANCELED" and state != "PENDING":
        print(f'Статус операции "{state}" недоступен.')
        state = input(":")
        state = state.upper()
    else:
        if state == "EXECUTED":
            print('Операции отфильтрованы по статусу "EXECUTED"')
        elif state == "CANCELED":
            print('Операции отфильтрованы по статусу "CANCELED"')
        else:
            print('Операции отфильтрованы по статусу "PENDING"')

    filter_trans = filter_by_state(trans, state)

    print("""Отсортировать операции по дате? Да/Нет""")
    data_filter = input(":").lower
    if data_filter == "да":
        while True:
            print("""Отсортировать по возрастанию или по убыванию?""")
            sort = input(":").lower()
            if sort == "по возрастанию":
                sorted_transaction_dict = sort_by_date(filter_trans, revers=False)
                break
            elif sort == "по убыванию":
                sorted_transaction_dict = sort_by_date(filter_trans)
                break
            else:
                print("Ответ введен не корректно")

    elif data_filter == "нет":
        sorted_transaction_dict = filter_trans

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")

        user_choose_rub = input(":").lower()

        if user_choose_rub == "да":
            sort_filtred_transaction_dict = filter_by_currency(filter_trans, "RUB")
            break
        elif user_choose_rub == "нет":
            sort_filtred_transaction_dict = filter_trans
            break
        else:
            print("Ответ введен некорректно")
            continue
    while True:
        print("Отфильтровать список транзакций по определенному слову" " в описании? Да/Нет")

        user_choose_word_filter = input(":").lower()

        if user_choose_word_filter == "да":
            print("Введите слово")
            search_word = input(":")
            word_filtred_transaction_dict = find_description(filter_trans, find_str=search_word)
            break
        elif user_choose_word_filter == "нет":
            word_filtred_transaction_dict = filter_trans
            break
        else:
            print("Ответ введен некорректно")
            continue

    print("Распечатываю итоговый список транзакций...")

    new_filter_trans = [*word_filtred_transaction_dict]
    if len(new_filter_trans) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(new_filter_trans)}")
        if menu == 1:
            for x in new_filter_trans:
                if x["description"] == "Открытие вклада":
                    print(f'{x["date"]} {x["description"]}')
                    pattern = r"\b\d+\b"
                    numer = re.findall(pattern, x["to"])
                    numer = "".join(numer)
                    print(f"Счет{get_mask_account(numer)}")
                    print(f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}')
                else:
                    print(f'{x["date"]} {x["description"]}')
                    pattern = r"\b\d+\b"
                    pattern1 = r"\b[A-Za-zА-Яа-яЁё]+\b"

                    text = x["from"]
                    numer_from = re.findall(pattern, text)
                    numer_from = "".join(numer_from)
                    name_from = re.findall(pattern1, text)
                    name_from = "".join(name_from)

                    text_to = x["to"]
                    numer_to = re.findall(pattern, text_to)
                    numer_to = "".join(numer_to)
                    name_to = re.findall(pattern1, text_to)
                    name_to = "".join(name_to)

                    if name_from == "Счет":
                        numer_from_mask = get_mask_account(numer_from)
                    else:
                        numer_from_mask = get_mask_card_number(numer_from)
                    if name_to == "Счет":
                        numer_to_mask = get_mask_account(numer_to)
                    else:
                        numer_to_mask = get_mask_card_number(numer_to)
                    print(f"{name_from} {numer_from_mask} -> {name_to} {numer_to_mask}")
                    print(f'Сумма: {x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}')
        else:
            for x in new_filter_trans:
                if x["description"] == "Открытие вклада":
                    print(f'{x["date"]} {x["description"]}')
                    pattern = r"\b\d+\b"
                    numer = re.findall(pattern, x["to"])
                    numer = "".join(numer)
                    print(f"Счет{get_mask_account(numer)}")
                    print(f'Сумма: {x["amount"]} {x["currency_name"]}')
                else:
                    print(f'{x["date"]} {x["description"]}')
                    pattern = r"\b\d+\b"
                    pattern1 = r"\b[A-Za-zА-Яа-яЁё]+\b"

                    text = x["from"]
                    numer_from = re.findall(pattern, text)
                    numer_from = "".join(numer_from)
                    name_from = re.findall(pattern1, text)
                    name_from = "".join(name_from)

                    text_to = x["to"]
                    numer_to = re.findall(pattern, text_to)
                    numer_to = "".join(numer_to)
                    name_to = re.findall(pattern1, text_to)
                    name_to = "".join(name_to)

                    if name_from == "Счет":
                        numer_from_mask = get_mask_account(numer_from)
                    else:
                        numer_from_mask = get_mask_card_number(numer_from)
                    if name_to == "Счет":
                        numer_to_mask = get_mask_account(numer_to)
                    else:
                        numer_to_mask = get_mask_card_number(numer_to)
                    print(f"{name_from} {numer_from_mask} -> {name_to} {numer_to_mask}")
                    print(f'Сумма: {x["amount"]} {x["currency_name"]}')


if __name__ == "__main__":
    main()
