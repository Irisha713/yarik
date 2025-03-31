import json


def transactions(path):
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding='utf=8') as file:
            data = json.load(file)
        if data:
            return data
        else:
            return []
    except FileNotFoundError or json.JSONDecodeError:
        return []
