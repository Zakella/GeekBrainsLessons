# 5. Дана строка в виде случайной последовательности чисел от 0 до 9.
# Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
# а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте функцию
# count_it(sequence), принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

import random
from collections import Counter
from itertools import islice


def count_it(sequence):
    print(sequence)
    lst = [int(i) for i in sequence]
    some_dict = {}
    most_comm = sorted(Counter(lst).most_common())
    for i in most_comm:
        some_dict[i[0]] = i[1]

    sorted_keys = sorted(some_dict, key=some_dict.get, reverse=True)
    sorted_dict = {}
    for w in sorted_keys:
        sorted_dict[w] = some_dict[w]

    return dict(islice(sorted_dict.items(), 3))


def random_string():
    string = ""
    for i in range(0, 9):
        string += str(random.randint(0, 9))
    return string


print(count_it(random_string()))
