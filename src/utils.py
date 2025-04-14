import json
import logging
import re
from collections import Counter

root_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../yarik/logs/utils.log", encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
root_logger.addHandler(file_handler)
root_logger.setLevel(logging.DEBUG)


def transactions(path):
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding='utf=8') as file:
            data = json.load(file)
        if data:
            root_logger.info("Возвращён список словарей")
            return data
        else:
            root_logger.error("Пустой файл")
            return []
    except FileNotFoundError or json.JSONDecodeError:
        root_logger.error("Ошибка")
        return []


def filter_list_dictionary1(lst, string):
    result = []
    for i in lst:
        for value in i.values():
            numbers = re.findall(string, str(value))
            if numbers != []:
                result.append(i)
    return result


def filter_list_dictionary2(lst1, lst2):
    lst = []
    for i in lst1:
        for key, value in i.items():
            if key == 'description' and value in lst2:
                lst.append(value)
    counted = Counter(lst)
    return counted
