from typing import Any

from masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> Any:
    """Возвращает строку с замаскированным номером"""
    if "Счет" in info:
        return get_mask_account(int(info[5:]))
    else:
        return get_mask_card_number(int(info[-16:]))


def get_date(date: str) -> Any:
    """возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    result = date[8:10] + "." + date[5:7] + "." + date[:4]
    return result
