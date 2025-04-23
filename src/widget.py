from typing import Any
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> Any:
    """Возвращает строку с замаскированным номером"""
    try:
        if info == "":
            return ""
        elif "Счет" in info:
            return f"Счет {get_mask_account(int(info[-20:]))}"
        else:
            return f"{info[:-16]}{get_mask_card_number(int(info[-16:]))}"
    except ValueError:
        return "Некорректный ввод"


def get_date(date: str) -> Any:
    """возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    try:
        if date == "":
            return ""
        result = date[8:10] + "." + date[5:7] + "." + date[0:4]
        return result
    except ValueError:
        return "Некорректный ввод"
