# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def count_febanaci(result, n, positive=True):
    if positive:
        start_1 = 0
        start_2 = 1
        n += -1
    else:
        start_1 = 1
        start_2 = 0

    for _ in range(n):
        if positive:
            number = start_1 + start_2
        else:
            number = start_1 - start_2

        start_1 = start_2
        start_2 = number
        result.append(number)


n = int(input("Введите число :"))

result_pos = []
result_pos.append(0)
count_febanaci(result_pos, n)
result_pos.remove(0)

result_neg = []
result_neg.append(0)
count_febanaci(result_neg, n, False)

print(list(reversed(result_neg)) + result_pos)
