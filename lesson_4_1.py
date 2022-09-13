# Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

accuracy = float(input(("Введите точность: ")))
number = str(float(input(("Введите число: "))))

accuracy = str(accuracy).split(".")[-1]
number_fraction = str(number).split(".")[-1]

if len(accuracy) > len(number_fraction):
    print(f'{number}{"0" * (len(accuracy) - len(number_fraction))}')
else:
    print(round(float(number), len(accuracy)))



