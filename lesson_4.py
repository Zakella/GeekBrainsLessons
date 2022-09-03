x = int(input("Введите номер четверти: "))

quarter = {
    1: "x,y",
    2: "- x,y",
    3: "- x,-y",
    4: "x,-y"
}

print(quarter.get(x))
