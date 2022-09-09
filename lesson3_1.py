# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#

import random
lst = []
for i in range(10):
    lst.append(random.randint(0, 9))

print(lst)

res = sum([lst[val] for val in range(1, len(lst), 2)])
print(res)


