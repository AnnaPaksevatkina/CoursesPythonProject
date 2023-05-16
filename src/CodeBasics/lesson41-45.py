# Lesson 41
# Приведите строку text к нижнему регистру и напечатайте её на экран.

text = 'a MIND needs Books as a Sword needS a WHETSTONE.'
lower_text = text.lower()
print(lower_text)

# Lesson 42
# Обновите переменную first_name, записав в неё то же самое значение, но обработанное методом .strip().
# Распечатайте то, что получилось, на экран.

first_name = '  Grigor   \n'
first_name = first_name.strip()
print(first_name)

# Lesson 43
# Найдите символы N и , (запятая) внутри текста в переменной text.
# Выведите на экран их индексы. Ожидаемый тестами вывод:
# Index Of N: 0
# Index Of ,: 25
# Ваша задача найти эти индексы в строке с помощью метода .find() и вставить в print(),
# не используя промежуточные переменные.
# Это упражнение можно решить как при помощи интерполяции, так и при помощи конкатенации.
# Если вы используете конкатенацию, то полученный результат необходимо привести к строковому типу.
# Для разбиения вывода на две строки, вам может понадобится \n.

text = 'Never forget what you are, for surely the world will not'
print(f"Index Of N: {text.find('N')}\nIndex Of ,: {text.find(',')}")

# Lesson 44
# С помощью среза строк получите часть предложения, записанного в переменную text, c 5 по 15 символы включительно.
# Полученную подстроку обработайте методом .strip() и выведите на экран длину итоговой подстроки.
# Выполните эти операции подряд в цепочке без создания промежуточных переменных.

text = 'When \t\n you play a \t\n game of thrones you win or you die.'
print(len(text[4:15].strip()))

# Lesson 45
# Реализуйте функцию с именем print_motto(), которая выведет на экран фразу Winter is coming.

def print_motto():
    print('Winter is coming')
