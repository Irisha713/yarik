import datetime
from src.utils import *
from src.processing import filter_by_state
from src.widget import *
from src.csv_xlsx_rader import *


def main():
    while True:
        print(f"""Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")
        user_file = input()
        if user_file == '1':
            print("Для обработки выбран JSON-файл.")
            data = transactions("../yarik/data/operations.json")
            break
        elif user_file == '2':
            print("Для обработки выбран CSV-файл.")
            data = read_transactions_from_csv("../yarik/data/transactions.csv")
            break
        elif user_file == '3':
            print("Для обработки выбран XLSX-файл.")
            data = read_transactions_from_excel("../yarik/data/transactions_excel.xlsx")
            break
        else:
            print("Некорректный ввод!")

    while True:
        print(f"""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        user_input = input()
        if user_input.upper() == 'EXECUTED':
            print('Операции отфильтрованы по статусу "EXECUTED"')
            break
        elif user_input.upper() == 'CANCELED':
            print('Операции отфильтрованы по статусу "CANCELED"')
            break
        elif user_input.upper() == 'PENDING':
            print('Операции отфильтрованы по статусу "PENDING"')
            break
        else:
            print(f'Статус операции "{user_input}" недоступен.')

    state_filter = filter_by_state(data)

    date_filter = input("Отсортировать операции по дате? Да/Нет ").title()
    if date_filter == 'Да':
        reverse_filter = input("Отсортировать по возрастанию или по убыванию? ").lower()
        if user_file == '1':
            if reverse_filter == 'по возрастанию':
                date_filter = sorted(state_filter, key=lambda x: datetime.strptime(x["date"],
                                    "%Y-%m-%dT%H:%M:%S.%f"))
                state_filter = date_filter
            elif reverse_filter == 'по убыванию':
                date_filter = sorted(state_filter, key=lambda x: datetime.strptime(x["date"],
                                    "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
                state_filter = date_filter
        if user_file == '2' or user_file == '3':
            if reverse_filter == 'по возрастанию':
                date_filter = sorted(state_filter, key=lambda x: datetime.strptime(x["date"],
                                    "%Y-%m-%dT%H:%M:%SZ"))
                state_filter = date_filter
            elif reverse_filter == 'по убыванию':
                date_filter = sorted(state_filter, key=lambda x: datetime.strptime(x["date"],
                                    "%Y-%m-%dT%H:%M:%SZ"), reverse=True)
                state_filter = date_filter


    rub_filter = input("Выводить только рублевые тразакции? Да/Нет ").title()
    if rub_filter == 'Да':
        rub_filter_func = filter_list_dictionary1(state_filter, 'RUB')
    else:
        rub_filter_func = state_filter

    word_filter = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет ").title()
    if word_filter == 'Да':
        user_word = input("Введите слово: ")
        word_filter_func = filter_list_dictionary1(state_filter, user_word)
    else:
        word_filter_func = state_filter

    total_operations = []

    for operation in word_filter_func:
        for dictionary in rub_filter_func:
            if operation == dictionary:
                total_operations.append(operation)

    print("Распечатываю итоговый список транзакций...")

    if total_operations != []:
        print(f"Всего банковских операций в выборке: {len(total_operations)}")
        print("")

        for i in total_operations:
            description = i.get("description")
            print(f"{get_date(i.get("date"))} {description}")
            if description == "Открытие вклада":
                print(mask_account_card(i.get("to")))
            else:
                print(f"{mask_account_card(i.get("from"))} -> {mask_account_card(i.get("to"))}")
            if user_file == "1":
                print(f"Сумма: {i.get("operationAmount").get("amount")} {i.get("operationAmount").get("currency").get("name")}")
            elif user_file == "2" or user_file == '3':
                print(f"Сумма: {i.get("amount")} {i.get("currency_code")}")
            print("")

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

if __name__ == "__main__":
    main()