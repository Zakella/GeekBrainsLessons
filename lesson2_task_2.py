# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import time

n = int(input("Please enter number:"))
result = []
temp_list = []
for i in range(1, n + 1):
    k = 1
    for j in temp_list:
        k += k * j
    temp_list.append(i)
    result.append(k)
print(result)
