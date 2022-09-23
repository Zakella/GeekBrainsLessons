# Задача 41: Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# #- Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:*
# 1+2*3 + 7 *10 *15 - 10  => 7;
# (1+2)*3 => 9;
# *Пример:*
# 2+2 => 4;#
# 1+2*3 => 7;#
# 1-2*3 => -5;


eval ()
def find_math_simb(lst, symb):
    if symb not in lst:
        return None
    else:
        return lst.index(symb)


def calculate(temp_list , expression):
    summ = 0

    priority = {
        "first_priority": ["*", "/"],
        "second_priority": ["-", "+"]
    }

    first_pr_list = []
    print(expression)
    print(temp_list)
    # for i in temp_list:
    #     print(i)
    # for i in range(len(expression)):
    #     for j in range(2, len(expression) - 1):
    #         print(j)
    #
    # for index, val in enumerate(expression):
    #     if index == len(expression)-1:
    #         print(val)
    #     if expression[index + 1] or expression[index-1] in priority.get("first_priority"):
    #         # first_pr_list.append(expression)


        # if val.isdigit() and index ==0:
        #     summ = float(val)
        # elif val.isdigit():

# some_expression = input("Введите выражение: ")
some_expression = "1+ 10 - 2*3  - 10 * 15 / 10"
# print(some_expression.split("+"))

# temp = some_expression.replace(" ", "").replace("*","#").replace("/", "#").replace("+", "#").replace("-", "#").split("#")
temp = some_expression.replace(" ", "").replace("+", "#").replace("-", "#").split("#")
# temp2 = some_expression.replace(" ", "").replace("*", "#").replace("/", "#").split("#")
# temp = some_expression.replace(" ", "").replace("+", "#").replace("-", "#")
calculate(temp, some_expression.replace(" ", ""))
# calculate(temp2, some_expression.replace(" ", ""))



# print(some_expression)

# print(some_expression.split("*"))

# full_lst = []
# # for i in some_expression.replace(" ",""):
#
#     # if i == "(":
#     #     lst = []
#     #     lst.append(i)
#     #
#     # print(i)
#
# # print(eval(some_expression))
#
# lst = [i for i in some_expression.replace(" ", "")]
# priorety = ["()", "*/", "+-"]
# full_lst = []
# print(lst)
# for ind, val in enumerate(lst):
#     if val == "(":
#         exp = []
#         while val != ")":
#             exp.append(lst[ind + 1])
#
#
#
#     if val == ")":
#         full_lst.append(exp)



# print(full_lst)

# print(some_expression.split("()"))
# math_simb = ["+", "-", "*", "/"]
#
#
# lst = [i for i in some_expression.replace(" ", "")]
# print(lst)
#
# for i in priorety:
#      p_start = find_math_simb(lst, i[0])
#      print(p_start)
# # p_start = find_math_simb(lst, "(")
# p_end = find_math_simb(lst, ")")

# if p_start != None and p_end != None:
#
#     # print(lst[p_start + 1: p_end])
#     list_inside = lst[p_start + 1: p_end]
#     summ = 0
#     for ind, val in enumerate(list_inside):
#         pass
# if val in math_simb:
#     if val == '+':
#         summ += int(list_inside[ind + 1])
#     elif val == '-':
#         summ -= int(list_inside[ind + 1])
#     elif val == '*':
#         summ *= int(list_inside[ind + 1])
#     elif val == '/':
#         summ *= int(list_inside[ind + 1])

# print(summ)

# symb = find_math_simb(lst[p_start + 1: p_end], val)
# print(ind, val)
# if not symb == None:
#     print(ind)

# for i in lst[p_start + 1: p_end]:
#     symb = find_math_simb(lst[p_start + 1: p_end], i)
#     if not symb == None:

# print(p_start)

# try:
#
#     p_start = lst.index("(")
#     p_end = lst.index(")")
#     # print(p_start, p_end)
#     print(lst[p_start + 1: p_end])
#     # for i in range(p_start + 1, p_end):
#     #     print(lst[i])
#     # # print(lst[p_start + 1][p_end -1])
#
# except ValueError:
#     pass
