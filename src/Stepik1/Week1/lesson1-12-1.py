# 1.12 Задачи по материалам недели

# Напишите программу, вычисляющую площадь треугольника по переданным длинам трёх его сторон по формуле Герона.
# На вход программе подаются целые числа, выводом программы должно являться
# вещественное число, соответствующее площади треугольника.

a = float(input())
b = float(input())
c = float(input())

p = ((a + b + c) / 2)

S = ((p * (p - a) * (p - b) * (p - c)) ** 0.5)

print(S)
