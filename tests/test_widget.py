from src.widget import get_date, mask_account_card


def test_mask_account_card(cards_and_accounts):
    assert mask_account_card(cards_and_accounts[0]) == 'Maestro 1596 83** **** 5199'
    assert mask_account_card(cards_and_accounts[1]) == 'Счет **9589'
    assert mask_account_card(cards_and_accounts[2]) == 'MasterCard 7158 30** **** 6758'
    assert mask_account_card(cards_and_accounts[3]) == 'Счет **5560'
    assert mask_account_card(cards_and_accounts[4]) == 'Visa Classic 6831 98** **** 7658'
    assert mask_account_card(cards_and_accounts[5]) == 'Visa Platinum 8990 92** **** 5229'
    assert mask_account_card(cards_and_accounts[6]) == 'Visa Gold 5999 41** **** 6353'
    assert mask_account_card(cards_and_accounts[7]) == 'Счет **4305'
    assert mask_account_card(cards_and_accounts[8]) == 'Некорректный ввод'


def test_mask_account_card_empty():
    assert mask_account_card('') == ''


def test_get_date(dates):
    assert get_date(dates[0]) == '11.03.2024'
    assert get_date(dates[1]) == '01.01.2000'
    assert get_date(dates[2]) == '31.12.1999'
    assert get_date(dates[3]) == 'Некорректный ввод'


def test_get_date_empty():
    assert get_date('') == ''