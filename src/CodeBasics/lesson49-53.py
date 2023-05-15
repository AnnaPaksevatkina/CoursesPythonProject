# Lesson 49
# Реализуйте функцию trim_and_repeat(), которая принимает три параметра: строку, offset — число символов,
# на которое нужно обрезать строку слева и repetitions — количество обрезанных строк, которые нужно вывести.
# Функция обрезает строку и повторяет ее столько раз, чтобы общее количество обрезанных строк равнялось repetitions.
# Функция должна записать результат в одну строку и вернуть его.
# Число символов для среза по умолчанию равно 0, а повторений — 1.
# text = 'python'
# print(trim_and_repeat(text, offset=3, repetitions=2)) # => honhon
# print(trim_and_repeat(text, repetitions=3)) # => pythonpythonpython
# print(trim_and_repeat(text)) # => python

def trim_and_repeat(text, offset=0, repetitions=1):
    return f'{text[offset:] * repetitions}'

# Lesson 50
# Реализуйте функцию letter_multiply(). Она должна принимать три параметра:
# Строку
# Символ
# Число, которое обозначает, сколько раз нужно повторить символ в слове
# text = 'python'
# print(letter_multiply(text, 'p', 2)) # => ppython
# print(letter_multiply(text, 'y' 3)) # => pyyython
# print(letter_multiply(text, 'n', 4)) # => pythonnnn
# Укажите аннотации типов при объявлении функции.

def letter_multiply(text: str, letter: str, repetitions: int) -> str:
    result = []
    for char in text:
        char = letter * repetitions if char == letter else char
        result.append(char)
    return ''.join(result)

# Lesson 51
# Напишите функцию is_pensioner(), которая принимает возраст в качестве единственного аргумента и проверяет,
# является ли этот возраст пенсионным. Пенсионным считается возраст 60 лет и больше.
# Примеры вызова:
# is_pensioner(75) # True
# is_pensioner(18) # False

def is_pensioner(age):
    return age >= 60

# Lesson 52
# Напишите функцию is_mister(), которая принимает строку и проверяет, является ли она словом 'Mister'.
# is_mister('Mister') # True
# is_mister('Missis') # False

def is_mister(string):
    return string == 'Mister'

# Lesson 53
# Реализуйте функцию is_international_phone(), которая проверяет формат указанного телефона.
# Если телефон начинается с +, значит это международный формат.
# is_international_phone('89602223423')  # False
# is_international_phone('+79602223423') # True

def is_international_phone(phone):
    return phone[0] == '+'