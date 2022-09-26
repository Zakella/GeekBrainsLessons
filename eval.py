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
        return float(exp1) * float(exp2)

    if symbol == '/':
        return float(exp1) / float(exp2)

    if symbol == '+':
        return float(exp1) + float(exp2)

    if symbol == '-':
        return float(exp1) - float(exp2)


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


inner_list = []
star_count = -1
used_indexes = []
for i in range(0, len(lst)):
    if lst[i] == "(":
        end = lst.index(")", star_count)
        if end not in used_indexes:
            inner_list.append((i, end))
            used_indexes.append(end)
        else:
            while True:
                end = lst.index(")", star_count)
                if end not in used_indexes:
                    inner_list.append((i, end))
                    used_indexes.append(end)
                    break
                star_count += -1


for i in reversed(inner_list):
    ind_start = i[0] + 1
    ind_end = i[1]
    lst[ind_end] = expression_result(expression_result(lst[ind_start: ind_end], first_priorety), second_priorety)[0]
    for j in range(ind_start -1, ind_end):
        lst[j] = "#"

print(expression_result(expression_result([i for i in lst if not i == "#"], first_priorety), second_priorety)[0])
print(eval(some_expression))
