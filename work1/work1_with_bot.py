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
name = input("Введите ваше имя и нажмите ENTER... ")
print(f"Добро пожаловать, {name}")


#print(casting_lots)


def pl1():
    global candy_count
    player1 = int(input(f"{name}, введите количество конфет (не более 28): "))
    if player1 <= 28:
        candy_count -= player1
    else:
        print(f"{name}, введите не более 28 конфет ")
        pl1()
    if candy_count < 1:
        input("Вы победили! ")


def bot_game():
    global candy_count
    if candy_count <= 28:
        player2 = candy_count
    else:
        player2 = random.randint(1, 28)
    print(f"Бот ввел число {player2}")
    if player2 <= 28:
        candy_count -= player2
    else:
        print(f"{name}, введите не более 28 конфет ")
        bot_game()

    if candy_count < 1:
        input("Бот победил! ")


def player():
    pl1()
    print(f"Осталось конфет - {candy_count}")


def bot():
    bot_game()
    print(f"Осталось конфет - {candy_count}")


def game():
    while candy_count > 0:
        player()
        bot()


def cast_lots():
    isCastlot = True
    if isCastlot:
        isCastlot = False
        casting_lots = random.randint(1, 2)

        if casting_lots == 1:
            print("По итогам жеребьевки первый ход делаете вы")
            player()
            bot()
        if casting_lots == 2:
            print("По итогам жеребьевки первый ход делает бот")
            bot()


cast_lots()
game()