# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst = [2, 3, 4, 5, 6]
print(len(lst) / 2)
result = []
last_ind = -1

for index, _ in enumerate(lst):
    numb = lst[last_ind] * lst[index]
    if numb not in result:
        result.append(numb)
    last_ind += - 1

print(result)

