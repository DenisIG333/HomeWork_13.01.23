# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота 'интеллектом'
import random

candy_count = 100


#print(casting_lots)


def pl1():
    global candy_count
    player1 = int(input("Первый игрок, введите количество конфет (не более 28): "))
    if player1 <= 28:
        candy_count -= player1
    else:
        print("Введите не более 28 конфет ")
        pl1()
    if candy_count < 1:
        input("Первый игрок победил! ")


def pl2():
    global candy_count
    player2 = int(input("Второй игрок, введите количество конфет (не более 28): "))
    if player2 <= 28:
        candy_count -= player2
    else:
        print("Введите не более 28 конфет ")
        pl2()

    if candy_count < 1:
        input("Второй игрок победил! ")


def player_1():
    pl1()
    print(f"Осталось конфет - {candy_count}")


def player_2():
    pl2()
    print(f"Осталось конфет - {candy_count}")


def game():
    while candy_count > 0:
        player_1()
        player_2()


def cast_lots():
    isCastlot = True
    if isCastlot:
        isCastlot = False
        casting_lots = random.randint(1, 2)

        if casting_lots == 1:
            print("По итогам жеребьевки первый ход игрока номер 1")
            player_1()
            player_2() #поскольку жребий выпал на первого игрока, следующий должен быть игрок 2
        if casting_lots == 2:
            print("По итогам жеребьевки первый ход игрока номер 2")
            player_2()


cast_lots()
game()
