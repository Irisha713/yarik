import csv

import pandas as pd


def read_transactions_from_csv(file_path: str) -> list[dict]:
    transactions = []
    """происходит считывание финансовых операций"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                transactions.append(dict(row))
        return transactions
    except Exception:
        raise Exception("Ошибка")


def read_transactions_from_excel(path):
    """роисходит считывание финансовых операций"""
    reader = pd.read_excel(path)
    transactions = reader.to_dict(orient='records')
    return transactions
