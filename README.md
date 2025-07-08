
# Домашнє Завдання з Python

## Завдання 1: Замикання і кешування чисел Фібоначчі

### Мета:
Реалізувати функцію `caching_fibonacci()`, яка повертає функцію `fibonacci(n)` з кешуванням обчислень за допомогою замикання.

### Вимоги:
- Створити зовнішню функцію `caching_fibonacci`, яка містить словник `cache`.
- Внутрішня функція `fibonacci(n)`:
  - Повертає `0`, якщо `n <= 0`.
  - Повертає `1`, якщо `n == 1`.
  - Якщо `n` в кеші — повертає значення з кешу.
  - Інакше обчислює `fibonacci(n-1) + fibonacci(n-2)`, зберігає в кеш і повертає результат.
- `caching_fibonacci()` повертає функцію `fibonacci`.

### Приклад використання:
```python
fib = caching_fibonacci()
print(fib(10))  # 55
print(fib(15))  # 610
```

---

## Завдання 2: Генератор чисел і підсумовування

### Мета:
Написати генератор дійсних чисел з тексту та функцію, що підраховує їхню суму.

### Вимоги:
- `generator_numbers(text: str)`:
  - Повертає **генератор** дійсних чисел, що витягуються з тексту.
  - Використовує `yield` та регулярні вирази для пошуку чисел (`re.findall()`).
- `sum_profit(text: str, func: Callable)`:
  - Приймає текст та функцію-генератор.
  - Повертає суму чисел, які генерує передана функція.

### Приклад:
```python
text = "Доходи: 1000.01, бонус: 27.45 і 324.00."
total = sum_profit(text, generator_numbers)
print(total)  # 1351.46
```

---

## Завдання 3 (необов’язкове): Аналіз лог-файлу

### Мета:
Реалізувати консольний скрипт, що аналізує лог-файл і виводить статистику.

### Вимоги:
- Запуск з консолі:
  ```bash
  python main.py /шлях/до/лог-файлу [рівень_логування]
  ```
- Парсинг рядків за форматом:
  ```
  [2024-07-07 15:12:34] ERROR File not found
  ```
- Реалізувати функції:
  - `parse_log_line(line: str) -> dict`
  - `load_logs(file_path: str) -> list`
  - `filter_logs_by_level(logs, level: str) -> list`
  - `count_logs_by_level(logs) -> dict`
  - `display_log_counts(counts: dict)`

### Вивід (таблиця):
```
Рівень логування | Кількість
-----------------|----------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1
```

### Приклад виклику:
```bash
python main.py logs.txt ERROR
```

---

## Завдання 4: Обробка помилок в боті-помічнику

### Мета:
Додати декоратор `input_error`, що обробляє помилки у функціях бота.

### Вимоги:
- Декоратор `input_error` має обробляти помилки:
  - `KeyError` → `"Enter user name"`
  - `ValueError` → `"Give me name and phone please"`
  - `IndexError` → `"Enter the argument for the command"`
- Декоратор застосовується до всіх функцій:
  - `add_contact`
  - `change_contact`
  - `get_phone`
  - `show_all`
- Повідомлення про помилку повертається з функції.

### Приклад реалізації:
```python
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter the argument for the command"
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
```

---

## ✅ Критерії оцінювання:

- Правильна реалізація логіки задач
- Ясна структура коду (функції, змінні, читабельність)
- Використання кешу/генераторів/regex
- Консольний запуск та обробка помилок
- Дотримання PEP8
