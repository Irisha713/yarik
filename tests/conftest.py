import pytest


@pytest.fixture
def cards():
    return [7000792289606361,
            5124364654134534,
            5431236466723452,
            1246335763453455,
            "bibika"]


@pytest.fixture
def accounts():
    return [70007922896063611523,
            51243646541345341563,
            54312364667234527422,
            12463357634534557644,
            "validol"]


@pytest.fixture
def cards_and_accounts():
    return [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
        "vzhik"
    ]


@pytest.fixture
def dates():
    return ["2024-03-11T02:26:18.671407",
            "2000-01-01T00:00:00.000000",
            "1999-12-31T23:59:59.999999",
            "kran"]


@pytest.fixture
def list_of_dictionaries():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
