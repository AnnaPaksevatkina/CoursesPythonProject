# 2.1 Цикл while

# Какое значение будет у переменной i после выполнения фрагмента программы?

i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2

# 13

#Сколько итераций цикла будет выполнено в этом фрагменте программы?

i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2
# 9

#Сколько всего знаков * будет выведено после исполнения фрагмента программы:

i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1
# 17


