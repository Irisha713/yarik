# Домашняя работа 10.1

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

# Пример использования filter_by_state
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)

# Пример использования sort_by_date
sorted_transactions = sort_by_date(transactions)
```

## Тестирование

В нашем проекте используется тестирование для обеспечения надёжности и корректности работы. Был использован фреймвор pytest.
Все написанные тесты находятся в папке tests, там же можно найти файл со всеми фикстурами в модуле "conftest.py"

Также вы можете ознакомиться с [метрикой](file:///C:/Users/Admin/Desktop/singularity%20(скрины)/coverage.PNG), которая показывает, какой процент кода программы был протестирован.