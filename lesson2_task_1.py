# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = float(input("Please enter number:"))
str_number = str(number).replace(".", "")
count = 0
for i in str_number:
    count += int(i)

print(count)
