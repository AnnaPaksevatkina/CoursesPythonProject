# Lesson 56
# Реализуйте функцию string_or_not(), которая проверяет является ли переданный параметр строкой.
# Если да, то возвращается 'yes' иначе 'no'
# string_or_not('Hexlet') # 'yes'
# string_or_not(10) # 'no'
# string_or_not('') # 'yes'
# string_or_not(False) # 'no'
# Проверить то, является ли переданный параметр строкой, можно при помощи функции isinstance():
# isinstance(3, str) # False
# isinstance('Hexlet', str) # True

def string_or_not(value):
    return isinstance(value, str) and 'yes' or 'no'


# Lesson 57
# Реализуйте функцию guess_number(), которая принимает число и проверяет,
# равно ли число заданному (пусть это будет 42).
# Если равно, то функция должна вернуть строку 'You win!',
# в противном случае нужно вернуть строку 'Try again!'.
# guess_number(42) # You win!
# guess_number(61) # Try again!

def guess_number(guess):
    if guess == 42:
        return 'You win!'
    return 'Try again!'


# Lesson 58
# Реализуйте функцию normalize_url(), которая выполняет нормализацию данных.
# Она принимает адрес сайта и возвращает его с https:// в начале.
# Функция принимает адреса в виде АДРЕС или http://АДРЕС, но всегда возвращает адрес в виде https://АДРЕС.
# На вход функции также может поступить адрес в уже нормализованном виде https://АДРЕС,
# в этом случае ничего менять не надо.
# Примеры вызова:
# print(normalize_url('https://ya.ru'))  # => 'https://ya.ru'
# print(normalize_url('google.com'))     # => 'https://google.com'
# print(normalize_url('http://ai.fi'))   # => 'https://ai.fi'
# Есть несколько способов решить задачу.
# Один из них — сравнивать первые 7 символов строки-аргумента со строкой http://,
# а потом на основе этого добавлять или не добавлять к ней https://.
# Также вам скорее всего потребуется отбросить ненужную часть в начале строки.
# Помните, мы рассматривали способ получения кусочка от строки с помощью среза? Если нет, напоминаю:
# Берём 6 символов от начала
# print('Winterfell'[:6])  # => 'Winter'
# Так вот, с помощью срезов можно также отбросить определённое количество символов:
# Отбрасываем первые 6 символов
# print('Winterfell'[6:])  # => 'fell'

def normalize_url(url):
    prefix = 'https://'
    if url[:8] == prefix:
        return url
    else:
        if url[:7] == 'http://':
            return prefix + url[7:]
        else:
            return prefix + url
