import os

import requests
from dotenv import load_dotenv


def conversion_currency(transaction) -> float:
    """Функция, конвертирующая сумму из иностранной валюты в рубли"""
    from_curr = transaction["operationAmount"]["currency"]["code"]
    amount = float(transaction["operationAmount"]["amount"])

    load_dotenv()
    access_key = os.getenv("API_KEY")

    headers = {"apikey": access_key}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_curr}&amount={amount}"

    if from_curr == "RUB":
        return amount
    elif from_curr != "RUB":
        result = requests.get(url, headers=headers)
        new_amount = result.json()
        return new_amount["result"]


if __name__ == "__main__":
    print(
        conversion_currency(
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        )
    )
