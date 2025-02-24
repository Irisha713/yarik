def get_mask_card_number(number_card: int) -> str:
    """Выводит замаскированный номер карты пользователя"""
    card_number = str(number_card)
    if card_number == '':
        return ''
    elif card_number.isdigit() and len(card_number) == 16:
        groups_of_card_number = [card_number[:4], card_number[4:6] + "**", "****", card_number[-4:]]
        result = ""
        for i in groups_of_card_number:
            result = result + i + " "
        return result[:-1]
    else:
        return 'Некорректный ввод'


def get_mask_account(number_account: int) -> str:
    """Выводит змаскированый счёт аккаунта пользователя"""
    account_number = str(number_account)
    if account_number == '':
        return ''
    elif account_number.isdigit() and len(account_number) == 20:
        result = "**" + account_number[-4:]
        return result
    else:
        return 'Некорректный ввод'
