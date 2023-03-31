# 1.12 Задачи по материалам недели

# Напишите программу, которая получает на вход три целых числа,
# по одному числу в строке, и выводит на консоль в три строки сначала максимальное,
# потом минимальное, после чего оставшееся число.
#
# На ввод могут подаваться и повторяющиеся числа.

a = int(input())
b = int(input())
c = int(input())

if (b < a > c > b) or (b == c and a > b):
    print(a, b, c, sep='\n')
elif (c < a > b > c) or (a == b and c < b):
    print(a, c, b, sep="\n")
elif (a < b > c > a) or (b == c and a < b):
    print(b, a, c, sep='\n')
elif (c < b > a > c) or (a == c and b > a):
    print(b, c, a, sep='\n')
elif (a < c > b > a) or (a == b and c > b):
    print(c, a, b, sep='\n')
elif (b < c > a > b) or (a == c and b < a):
    print(c, b, a, sep='\n')
else:
    print(a, b, c, sep='\n')
