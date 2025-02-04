from masks import get_mask_card_number, get_mask_account

def mask_account_card(info: str) -> str:
    """Возвращает строку с замаскированным номером"""
    if "Счет" in info:
        return get_mask_account(int(info[5:]))
    else:
        return get_mask_card_number(int(info[-16:]))
