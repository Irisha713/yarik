# Домашняя работа 14.1

## Описание:

В этом проекте находится виджет банковских операций.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/username/project.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```

3. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

4. Запустите локальный сервер:
```
python manage.py runserver
```
## Использование:

Примеры использования функций:

```python
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from tests.conftest import transactions
import pandas as pd
import csv

# Пример использования filter_by_state
transactions1 = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions1)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions1)

# Пример использования filter_by_currency
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
# Пример использования read_transactions_from_csv
def read_transactions_from_csv(file_path: str) -> list[dict]:
    transactions = []
    """происходит считывание финансовых операций"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter= ';')
            for row in reader:
                transactions.append(dict(row))
        return transactions
    except FileNotFoundError:
        raise ModuleNotFoundError(f"Файл не найден")
    except Exception as e:
        raise Exception(f"Ошибка")
# Пример использования read_transactions_from_excel
def read_transactions_from_excel(path):
    """роисходит считывание финансовых операций"""
    reader = pd.read_excel(path)
    transactions = reader.to_dict(orient='records')
    return transactions 
```

## Тестирование

В нашем проекте используется тестирование для обеспечения надёжности и корректности работы. Был использован фреймвор pytest.
Все написанные тесты находятся в папке tests, там же можно найти файл со всеми фикстурами в модуле "conftest.py"

```
File	        statements  missing  excluded   coverage
src\__init__.py	    0	        0       0         100%
src\decorators.py   20          3       0         85%
src\generators.py   9           0       0         100%
src\masks.py	    19	        0       0         100%
src\processing.py   17	        2       0         88%
src\widget.py	    20	        0       0         100%
Total	            85	        5       0         94%
```