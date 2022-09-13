# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

some_list = [1, 5, 5, 7, 12, -3, 1, -3, 8, 7]
print(list(set(some_list)))#Первый способ

unic_list = []

for i in some_list:
    if i not in unic_list:
        unic_list.append(i)

print(unic_list)  # второй способ
