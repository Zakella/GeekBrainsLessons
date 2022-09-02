# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = input("Введите x: ")
y = input("Введите y: ")
z = input("Введите z: ")

expression1 = not (x or y or z)
expression2 = not x and not y and not z
print(expression1 == expression2)
