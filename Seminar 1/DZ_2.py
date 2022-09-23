# Задача 2
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# 1 вариант
def log (x, y, z):
    left = not(x or y or z)
    right = not x and not y and not z
    return left == right

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'x: {x}, y: {y}, z: {z}')
            print(log(x, y, z))


# 2 вариант
x = int(input("Введите первое значение: "))
y = int(input("Введите второе значение: "))
z = int(input("Введите третье значение: "))

if not(x or y or z) == (not x and not y and not z):
    print('Утверждение верно')
else:
    print('Утверждение ложно')