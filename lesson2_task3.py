# Задайте
# список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:

n = int(input("Please enter number:"))

dct = {}
for i in range(1, n + 1):
    dct[i] = int((1 + 1 / i) * i)

print(dct)
