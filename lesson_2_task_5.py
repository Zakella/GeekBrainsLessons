# Реализуйте алгоритм перемешивания спискa

import random

n = int(input("Please enter number:"))

lst = []
for i in range(1, n + 1):
    lst.append(i)

random.shuffle(lst)
print(lst)
