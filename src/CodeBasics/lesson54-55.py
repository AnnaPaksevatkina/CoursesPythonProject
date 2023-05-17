# Lesson 54
# Реализуйте метод is_leap_year(), который определяет является ли год високосным или нет.
# Год будет високосным, если он кратен (то есть делится без остатка) 400 или он одновременно кратен 4 и не кратен 100.
# Как видите, в определении уже заложена вся необходимая логика, осталось только переложить её на код:
# is_leap_year(2018) # false
# is_leap_year(2017) # false
# is_leap_year(2016) # true
# Кратность можно проверять так:
# % - возвращает остаток от деления левого операнда на правый
# Проверяем что number кратен 10
# number % 10 == 0
# Проверяем что number не кратен 10
# number % 10 != 0

def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

# Lesson 55
# В этом уроке вам нужно будет реализовать две функции is_palindrome() и is_not_palindrome()
# Реализуйте функцию is_palindrome(), которая определяет, является ли слово палиндромом или нет.
# Палиндром - это слово, которое читается одинаково в обоих направлениях.
# Слова в функцию могут быть переданы в любом регистре,
# поэтому сначала нужно привести слово к нижнему регистру: word.lower().
# is_palindrome('шалаш') # true
# is_palindrome('хекслет') # false
# is_palindrome('Довод') # true
# is_palindrome('Функция') # false
# Реализуйте функцию is_not_palindrome(), которая проверяет что слово НЕ является палиндромом:
# is_not_palindrome('шалаш') # false
# is_not_palindrome('Ага') # false
# is_not_palindrome('хекслет') # true
# Для этого, вызовите функцию is_palindrome() внутри is_not_palindrome() и примените отрицание.

def is_palindrome(word):
    lower_word = word.lower()
    return lower_word == lower_word[::-1]


def is_not_palindrome(word):
    return not is_palindrome(word)