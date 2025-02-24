from datetime import datetime


def filter_by_state(list_of_dictionaries: list, state: str = 'EXECUTED') -> list:
    """Функция возвращает новый список словарей,
    у которых ключ state
    соответствует указанному значению."""
    new_list = []
    for dictionary in list_of_dictionaries:
        for key, value in dictionary.items():
            if key == "state" and value == state:
                new_list.append(dictionary)

    return new_list


def sort_by_date(list_of_dictionaries: list, reverse_state: bool = False) -> list:
    """Возвращает новый список словарей,
    отсортированный по дате"""

    def sort(dictionary: dict) -> datetime:
        """Преобразует строку даты"""
        return datetime.strptime(dictionary["date"], "%Y-%m-%dT%H:%M:%S.%f")

    new_list = sorted(list_of_dictionaries, key=sort, reverse=not reverse_state)
    return new_list
