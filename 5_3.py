# Создайте программу для игры в ""Крестики-нолики"".
from numpy import unique


def start_new_game():
    a = 3
    mas = ["#"] * a
    for i in range(a):
        mas[i] = ["#"] * a
    return mas


def show_desk():
    for i in desk:
        for i2 in i:
            print(i2, end=' ')
        print()


def check_diagonally(desk):
    return False


def check_vertically(desk):
    return False


def check_horizontally(desk):
    for i in desk:
        unic_lst = list(set(i))
        if len(unic_lst) == 1 and not "#" in unic_lst:
            send_congratulation(unic_lst)
            return True
    return False


def send_congratulation(unic_lst):
    if unic_lst[0] == "x":
        print("Поздравляем! Игрок №1 победил!")
    else:
        print("Поздравляем! Игрок №2 победил!")


desk = start_new_game()

print(desk)
show_desk()

game_over = False
next_move = True

while not game_over:

    if next_move:
        player1_move = input('Игрок № 1 введите номер колонки, затем номер строки для хода: ')
        symb = "x"
        move = player1_move.split()
    else:
        player2_move = input('Игрок № 2 введите номер колонки, затем номер строки для хода: ')
        symb = "0"
        move = player2_move.split()

    for i, val in enumerate(desk):
        # print(i, val)
        move_x = int(move[0])
        move_y = int(move[1])
        if desk[move_y - 1][move_x - 1] == "#":
            desk[move_y - 1][move_x - 1] = symb
            next_move = not next_move
            break
        else:
            print("Место уже занято , сделайте ход еще раз!")
            break

    game_over = check_horizontally(desk)
    game_over = check_vertically(desk)
    game_over = check_diagonally(desk)
    show_desk()

    if game_over:
        print("Игра окончена")
