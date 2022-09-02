# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))

expression1 = x + y + z
expression2 = x * y
print(expression1 == expression2)
