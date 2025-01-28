import pandas as pd


def read_transactions_from_csv(filename: str) -> list[dict]:
    """Считывание финансовых операций из CSV-файлов."""
    if len(filename) == 0 or not isinstance(filename, str):
        return []
    try:
        df = pd.read_csv(filename, delimiter=";")  # для чтения файла
        dict_list = df.to_dict(orient="records")  # преобразование в list[dict]
        return dict_list
    except FileNotFoundError:
        return []
    except pd.errors.EmptyDataError:  # пустой файл
        return []
    except pd.errors.ParserError:  # неверный формат
        return []


def read_transactions_from_excel(filename: str) -> list[dict]:
    """Считывание финансовых операций из XLSX-файлов."""
    if len(filename) == 0 or not isinstance(filename, str):
        return []
    try:
        df = pd.read_excel(filename)
        dict_list = df.to_dict(orient="records")
        return dict_list
    except FileNotFoundError:
        return []
    except pd.errors.EmptyDataError:  # пустой файл
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []
