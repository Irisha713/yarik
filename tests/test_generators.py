import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

def test_filter_by_currency_usd(transactions):
    expected_result = [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }]
    usd_transactions = filter_by_currency(transactions, "USD")
    result = []
    for _ in range(2):
        result.append(next(usd_transactions))
    assert result == expected_result


def test_filter_by_currency_rub(transactions):
    expected_result = [{
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
    rub_transactions = filter_by_currency(transactions, "RUB")
    result =[]
    for _ in range(2):
        result.append(next(rub_transactions))
    assert result == expected_result

def test_transactions_description(transactions):
    expected_result = """Перевод организации
Перевод со счета на счет
Перевод со счета на счет
Перевод с карты на карту
Перевод организации\n"""
    descriptions = transaction_descriptions(transactions)
    result = ''
    for _ in range(5):
        result = result + (f"{next(descriptions)}\n")
    assert result == expected_result


@pytest.mark.parametrize("first_number, last_number, expected_result", [
    (90, 92, ["0000 0000 0000 0090", "0000 0000 0000 0091", "0000 0000 0000 0092"]),
    (57, 59, ["0000 0000 0000 0057", "0000 0000 0000 0058", "0000 0000 0000 0059"]),
    (745, 747, ["0000 0000 0000 0745", "0000 0000 0000 0746", "0000 0000 0000 0747"])
])
def test_card_number_generator(first_number, last_number, expected_result):
    assert list(card_number_generator(first_number, last_number)) == expected_result