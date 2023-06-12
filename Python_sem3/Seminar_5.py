# Задача на семинаре
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

from random import randint
numbers = []
for i in range(1, 13, 3):
    numbers.append(randint(1, 8))

print(f'{numbers}')
#
# for elem in set(numbers):
#     if numbers.count(elem) == 2:
#         for _ in range(2):
#             numbers.remove(elem)
# print(f'{numbers}')
