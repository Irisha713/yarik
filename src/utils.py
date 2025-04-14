import json
import logging

root_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/utils.log")
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
