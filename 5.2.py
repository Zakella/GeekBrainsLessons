# #Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#  a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

SWEETS = 20
MAX_MOVE = 4

next_move = random.randint(1, 2)
dct = {
    1: 0,
    2: 0

}

bot_in_game = input('Вместо второго игрока подключить бота (y/n)?: ')
bot_in_game = True if bot_in_game == "y" else False
print(f'Итого {SWEETS} конфеты. Начинаем игру!')

while True:
    if SWEETS <= MAX_MOVE:
        print(f'Осталось {SWEETS} конфет, игрок №{next_move} автоматически забирает все конфеты')
        break

    if next_move == 1:
        move_value = int(input('Игрок №1 ваш ход: '))
    else:
        if bot_in_game:
            move_value = random.randint(1, MAX_MOVE)
            print(f'Бот сделал ход и забрал {move_value} конфет')
        else:
            move_value = int(input('Игрок №2 ваш ход: '))

    if move_value > MAX_MOVE:
        print("Не верный ход, повторите еще раз")
        continue

    next_move = 2 if next_move == 1 else 1
    dct[next_move] += move_value

    SWEETS -= move_value
    print()
    print(f'Осталось {SWEETS} конфет. \n'
          f'Игрок №1 {dct.get(1)} конфет \n'
          f'Игрок №2 {dct.get(2)} конфет')

    print()

print(f'Поздравляем игрока №{next_move} с победой!')
