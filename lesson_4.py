#Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input("Введите номер четверти: "))

quarter = {
    1: "x,y",
    2: "- x,y",
    3: "- x,-y",
    4: "x,-y"
}

print(quarter.get(x))
