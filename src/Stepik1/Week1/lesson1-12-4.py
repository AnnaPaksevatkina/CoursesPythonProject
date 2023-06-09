# 1.12 Задачи по материалам недели

# Жители страны Малевии часто экспериментируют с планировкой комнат.
# Комнаты бывают треугольные, прямоугольные и круглые.
# Чтобы быстро вычислять жилплощадь, требуется написать программу,
# на вход которой подаётся тип фигуры комнаты и соответствующие параметры,
# которая бы выводила площадь получившейся комнаты.
# Для числа π в стране Малевии используют значение 3.14.
# Формат ввода, который используют Малевийцы:
# треугольник, где a, b и c — длины сторон треугольника
# прямоугольник, где a и b — длины сторон прямоугольника
# круг, где r — радиус окружности

room = input()

if room == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)

elif room == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a * b)

elif room == 'круг':
    r = float(input())
    print(3.14 * r ** 2)
