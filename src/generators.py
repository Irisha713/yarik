def filter_by_currency(list_dictionary, currency):
    """принимает на вход список словарей, представляющих транзакции"""
    return (
        transaction
        for transaction in list_dictionary
        if transaction.get("operationAmount").get("currency").get("code") == currency
    )


def transaction_descriptions(list_dictionary):
    """принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in list_dictionary:
        yield transaction.get("description")


def card_number_generator(first_number, last_number):
    """который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX
    , где
    X
     — цифра номера карты."""
    for num in range(first_number, last_number + 1):
        card = f"{num:016d}"
        yield " ".join([card[i:i + 4] for i in range(0, 16, 4)])
