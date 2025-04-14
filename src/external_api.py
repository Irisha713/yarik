import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_TOKEN")

def get_amount(transaction):
    """принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    amount = float(transaction.get('operationAmount').get('amount'))
    code = transaction.get('operationAmount').get('currency').get('code')

    if code == 'RUB':
        return amount

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={code}&amount={amount}"

    payload = {}
    headers = {
        "apikey": api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    if status_code == 200:
        result = response.json()
        return result['result']
