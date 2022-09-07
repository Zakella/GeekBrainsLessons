#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Please enter number:"))

lst = []
for i in range(-n, n + 1):
    lst.append(i)

with open("index.txt", "r") as f:
    result = 1
    for line in f.readlines():
        print(lst[int(line)])
        result += result * lst[int(line)]
        # for i in lst:

        # print(line, end="")
#
# for i in lst:
#
print(result)
# print(lst)