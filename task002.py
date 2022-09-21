# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите).
#  Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random
number_candies = 202

def game_candies(number_candies):

    a = random.randint(0, 1)


    while (number_candies > 0):
        if a % 2 == 0:
            players = 1
        else:
            players = 2
        print(f'ходит {players} игрок')
        candies = int(input())
        number_candies -= candies
        print(number_candies)
        a = a + 1
    if number_candies <= 0 and players == 1:
        print('Выйграл 2 игрок')
    elif number_candies <= 0 and players == 2:
        print('Выйграл 1 игрок')

game_candies(number_candies)