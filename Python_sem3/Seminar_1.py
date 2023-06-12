# Задача на семинаре
# ✔ Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.
from random import randint
numbers = []
for i in range(30):
    numbers.append(randint(1, 10))

numbers2 = []
for val in numbers:
    if val not in numbers2:
        numbers2.append(val)

numbers3 = set(numbers)


print(f'{numbers}\n{numbers2}\n{numbers3}')
