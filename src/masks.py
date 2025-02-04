def get_mask_card_number(number_card: int) -> str:
    """Выводит замаскированный номер карты пользователя"""
    card_numbers = [str(number_card)[:4], str(number_card)[4:6]+'**', '****', str(number_card)[-4:]]
    result = ''
    for i in card_numbers:
        result = result + i + ' '
    return result


def get_mask_account(number_account: int) -> str:
    """Выводит змаскированый счёт аккаунта пользователя"""
    result = '**' + str(number_account)[-4:]
    return result


print(get_mask_card_number(7000792289606361))
print(get_mask_account(73654108430135874305))
