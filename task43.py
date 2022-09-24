# Задача 43: Дана последовательность чисел. Получить список
# уникальных элементов заданной последовательности.
#
# Пример:
#
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

lst = [1, 2, 3, 5, 1, 5, 3, 10]
repeat_list = []
result = []
for index, value in enumerate(lst):
    for i in lst[index+1: len(lst)]:
        if value == i:
            repeat_list.append(i)
            break

    if value not in repeat_list:
        result.append(value)

print(result)
