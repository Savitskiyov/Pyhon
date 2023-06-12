# Задача на семинаре
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

from random import randint
numbers = []
for i in range(13):
    numbers.append(randint(1, 8))

print(f'{numbers}')

for elem in set(numbers):
    if numbers.count(elem) == 2:
        for _ in range(2):
            numbers.remove(elem)
print(f'{numbers}')
