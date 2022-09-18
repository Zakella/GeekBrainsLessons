# Создайте программу для игры в ""Крестики-нолики"".

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
    if check_list_for(desk[0][-1], desk[1][1], desk[2][0]) or check_list_for(desk[0][0], desk[1][1], desk[2][-1]):
        return True
    else:
        return False


def check_list_for(*args):
    check_list = [i for i in args]
    if "#" not in check_list:
        check_list = list(set(check_list))
        if len(check_list) == 1:
            send_congratulation(check_list[0])
            return True

    return False


def check_vertically(desk):
    res = list(zip(desk[0], desk[1], desk[2]))
    for i in res:
        i = list(set(i))
        if "#" not in i:
            if len(i) == 1:
                send_congratulation(i[0])
                return True
    return False


def check_horizontally(desk):
    for i in desk:
        unic_lst = list(set(i))
        if len(unic_lst) == 1 and not "#" in unic_lst:
            send_congratulation(unic_lst[0])
            return True
    return False


def check_draw(desk):
    all = []
    for i in desk:
        all += i
    if not "#" in all:
        print("К сожалению у вас ничья :( Начните снова!")
        return True
    return False


def send_congratulation(symb):
    if symb == "x":
        print("Поздравляем! Игрок №1 победил!")
    else:
        print("Поздравляем! Игрок №2 победил!")


desk = start_new_game()
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
    if game_over:
        break

    game_over = check_vertically(desk)
    if game_over:
        break

    game_over = check_diagonally(desk)
    if game_over:
        break

    game_over = check_draw(desk)
    if game_over:
        break

    show_desk()

if game_over:
    show_desk()
    print("Игра окончена")
