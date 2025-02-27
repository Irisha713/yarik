def filter_by_currency(list_dictionary, currency):
    return (transaction for transaction in list_dictionary
            if transaction.get("operationAmount").get("currency").get("code") == currency)


def transaction_descriptions(list_dictionary):
    for transaction in list_dictionary:
        yield transaction.get("description")


def card_number_generator(first_number, last_number):
    for num in range(first_number, last_number+1):
        card = f"{num:016d}" #0000000000000013
        yield ' '.join([card[i:i+4] for i in range(0, 16, 4)])
