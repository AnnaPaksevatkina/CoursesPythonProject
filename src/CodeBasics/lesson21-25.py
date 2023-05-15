# Lesson 21
# Напишите программу, которая берет исходное количество евро, записанное в переменную euros_count,
# переводит евро в доллары и выводит на экран.
# Затем полученное значение переводит в рубли и выводит на новой строчке.
# Пример вывода для 100 евро:
# 125.0
# 7500.0
# Считаем, что:
# - 1 евро = 1.25 долларов
# - 1 доллар = 60 рублей

euros_count = 100
dollars_count = euros_count * 1.25
print(dollars_count)
rubles_count = dollars_count * 60
print(rubles_count)

# Lesson 22
# Напишите программу, которая будет генерировать заголовок и тело письма,
# используя уже готовые переменные, и выводить получившиеся строки на экран.
# Для заголовка используйте переменные first_name и greeting, запятую и восклицательный знак.
# Выведите это на экран в правильном порядке.
# Для тела письма используйте переменные info и intro, при этом второе предложение должно быть на новой строке.
# Результат на экране будет выглядеть так:
# Hello, Joffrey!
# Here is important information about your account security.
# We couldn't verify your mother's maiden name.
# Выполните задание, используя только два print().

info = "We couldn't verify your mother's maiden name."
intro = "Here is important information about your account security."

first_name = 'Joffrey'
greeting = 'Hello'
print(greeting + ", " + first_name + "!")
print(intro + "\n" + info)

# Lesson 23
# Создайте две переменные с именами «первое число» и «второе число» на английском языке используя snake_case.
# Запишите в первую переменную число 20, во вторую — -100.
# Выведите на экран произведение чисел, записанных в получившиеся переменные.

first_number = 20
second_number = -100
print(first_number * second_number)

# Lesson 24
# Избавьтесь от магических чисел, создав новые переменные, а затем выведите текст на экран.
# Получится так:
# Rooms in King Balon's Castle:
# 102

king = "Rooms in King Balon's Castle:"
number_of_castles = 6
rooms_per_castle = 17
print(king)
print(number_of_castles * rooms_per_castle)

# Lesson 25
# Создайте константу DRAGONS_BORN_COUNT и запишите в неё число 3 — это количество драконов, родившихся у Дайенерис.

DRAGONS_BORN_COUNT = 3