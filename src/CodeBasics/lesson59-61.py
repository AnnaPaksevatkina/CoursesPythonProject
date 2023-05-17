# Lesson 59
# На электронной карте Вестероса, которую реализовал Сэм,
# союзники Старков отображены зелёным кружком, враги — красным, а нейтральные семьи — серым.
# Напишите для Сэма функцию who_is_this_house_to_starks(),
# которая принимает на вход фамилию семьи и возвращает одно из трёх значений: 'friend', 'enemy', 'neutral'.
# Правила определения:
# Друзья ('friend'): 'Karstark', 'Tully'
# Враги ('enemy'): 'Lannister', 'Frey'
# Любые другие семьи считаются нейтральными ('neutral')
# Примеры вызова:
# print(who_is_this_house_to_starks('Karstark'))  # => 'friend'
# print(who_is_this_house_to_starks('Frey'))      # => 'enemy'
# print(who_is_this_house_to_starks('Joar'))      # => 'neutral'
# print(who_is_this_house_to_starks('Ivanov'))    # => 'neutral'

def who_is_this_house_to_starks(house_name):
    if house_name == 'Karstark' or house_name == 'Tully':
        return 'friend'
    elif house_name == 'Lannister' or house_name == 'Frey':
        return 'enemy'
    return 'neutral'


# Lesson 60
# Реализуйте функцию flip_flop(), которая принимает на вход строку и,
# если эта строка равна 'flip', возвращает строку 'flop'.
# В противном случае функция должна вернуть 'flip'.
# Примеры вызова:
# print(flip_flop('flip'))  # => 'flop'
# print(flip_flop('flop'))  # => 'flip'

def flip_flop(arg):
    return 'flop' if arg == 'flip' else 'flip'


# Lesson 61
# Реализуйте функцию get_number_explanation(), которая принимает на вход число и возвращает объяснение этого числа.
# Если для числа нет объяснения, то возвращается just a number. Объяснения есть только для следующих чисел:
# 666 - devil number
# 42 - answer for everything
# 7 - prime number
# Примеры вызова функции:
# get_number_explanation(8)  # just a number
# get_number_explanation(666)  # devil number
# get_number_explanation(42)  # answer for everything
# get_number_explanation(7)  # prime number

def get_number_explanation(number):
    match number:
        case 666:
            return 'devil number'
        case 7:
            return 'prime number'
        case 42:
            return 'answer for everything'
        case _:
            return 'just a number'

