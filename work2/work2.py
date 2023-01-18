# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

playing_field = list(range(1, 10))


def start_game(field):
    counter = 0
    is_win = False
    while not is_win:
        draw_field(field)
        if counter % 2 == 0:
           check_input("X")
        else:
           check_input("O")
        counter += 1
        if counter > 4:
           temp = if_win(field)
           if temp:
              print(temp, "Победил")
              is_win = True
              break
        if counter == 9:
            print("Ничья")
            break
    draw_field(field)

def draw_field(field):
   print("—" * 13)
   for i in range(3):
       print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
       print("—" * 13)


def check_input(token):
   isInput = False
   while not isInput:
      input_player = input(f"Выберите номер ячейки для {token} ")
      try:
         input_player = int(input_player)
      except:
         print("Вы ввели не число")
         continue
      if input_player >= 1 and input_player <= 9:
         if(str(playing_field[input_player - 1]) not in "XO"):
            playing_field[input_player - 1] = token
            isInput = True
         else:
            print("Эта клетка занята")
      else:
        print("Введите число от 1 до 9.")


def if_win(field):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if field[each[0]] == field[each[1]] == field[each[2]]:
          return field[each[0]]
   return False


start_game(playing_field)
