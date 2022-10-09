# 2 Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения;
# 2) с помощью дополнительных библиотек Python.


# 1 вариант
a = int(input("Введите число a:"))
b = int(input("Введите число b:"))
c = int(input("Введите число x:"))

my_list = (a, b, c)

def descriminant (inpute_my_list):
    a, b, c = inpute_my_list
    d = b ** 2 - 4 * a * c
    if d == 0:
        x1 = -b / 2 * a
        return x1, None
    elif d > 0:
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
        return x1, x2
    else:
        # print('Уравнение не имеет корней')
        return None, None
print (descriminant(my_list))
# 2 вариант

import cmath

a = int(input("Введите число a:"))
b = int(input("Введите число b:"))
c = int(input("Введите число x:"))

d = (b ** 2) - (4 * a * c)


sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)
print(sol1, sol2)
