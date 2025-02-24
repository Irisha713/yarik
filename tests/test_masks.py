from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(cards):
    assert get_mask_card_number(cards[0]) == '7000 79** **** 6361'
    assert get_mask_card_number(cards[1]) == '5124 36** **** 4534'
    assert get_mask_card_number(cards[2]) == '5431 23** **** 3452'
    assert get_mask_card_number(cards[3]) == '1246 33** **** 3455'
    assert get_mask_card_number(cards[4]) == 'Некорректный ввод'


def test_get_mask_card_number_empty():
    assert get_mask_card_number('') == ''


def test_get_mask_account(accounts):
    assert get_mask_account(accounts[0]) == '**1523'
    assert get_mask_account(accounts[1]) == '**1563'
    assert get_mask_account(accounts[2]) == '**7422'
    assert get_mask_account(accounts[3]) == '**7644'
    assert get_mask_account(accounts[4]) == 'Некорректный ввод'


def test_get_mask_account_empty():
    assert get_mask_account('') == ''