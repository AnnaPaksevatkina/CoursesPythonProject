# 1.10 Условия: if, else, elif. Блоки, отступы

# Требуется определить, является ли данный год високосным.
# Напомним, что високосными годами считаются те годы, порядковый номер которых либо кратен 4,
# но при этом не кратен 100, либо кратен 400 (например, 2000-й год являлся високосным, а 2100-й будет невисокосным годом).
# Программа должна корректно работать на числах 1900≤n≤3000.
# Выведите "Високосный" в случае, если считанный год является високосным
# и "Обычный" в обратном случае (не забывайте проверять регистр выводимых программой символов).

year = int(input())
if (4 != 0 or 100 == 0) and 400 != 0:
    print('Обычный')
else:
    print('Високосный')
