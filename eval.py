# Задача 41: Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# #- Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:*
# 1+2*3 + 7 *10 *15 - 10  => 7;
# (1+2)*3 => 9;
# *Пример:*
# 2+2 => 4;#
# 1+2*3 => 7;#
# 1-2*3 => -5;

def calculate(exp1, symbol, exp2):
    if symbol == '*':
        return int(exp1) * int(exp2)

    if symbol == '/':
        return int(exp1) / int(exp2)

    if symbol == '+':
        return int(exp1) + int(exp2)

    if symbol == '-':
        return int(exp1) - int(exp2)


def split_numbers(string):
    res = ""
    for i in string:
        if i.isdigit():
            res += i
        else:
            break
    return res


def expression_result(lst, priorety):
    for ind, _ in enumerate(lst):
        if not ind == len(lst) - 1:
            symbol = lst[ind]
            if symbol in priorety:
                lst[ind + 1] = calculate(lst[ind - 1], lst[ind], lst[ind + 1])
                lst[ind] = "#"
                lst[ind - 1] = "#"

    return [i for i in lst if not i == "#"]


some_expression = input("Введите выражение: ").replace(" ", "")
# some_expression = "10 + (0 + (15 + 20) *3)".replace(" ", "")
first_priorety = ["*", "/"]
second_priorety = ["+", "-"]
lst = []
skip = False
for ind, val in enumerate(some_expression):
    if val.isdigit():
        if not skip:
            lst.append(split_numbers(some_expression[ind:len(some_expression)]))
            skip = True
    else:
        lst.append(val)
        skip = False

for index, val in enumerate(lst):
    if val == "(":
        i1 = index + 1
        i2 = lst.index(")", i1)
        lst[i2] = expression_result(expression_result(lst[i1:i2], first_priorety), second_priorety)[0]
        for j in range(index, i2):
            lst[j] = "#"

print(expression_result(expression_result([i for i in lst if not i == "#"], first_priorety), second_priorety)[0])
print(eval(some_expression))