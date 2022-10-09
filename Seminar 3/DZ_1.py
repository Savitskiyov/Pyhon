# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# 1 вариант
import random

spisok = []
spisok2 = []
for i in range(0,8):
    spisok.append(random.randint(1,20))
print(spisok)

for ind, element in enumerate(spisok, start=0):
    if ind % 2 == 1:
        spisok2.append(element)
print(spisok2)
print(sum(spisok2))


# 2 вариант
list = [2, 3, 5, 9, 3]
res = 0
for i in range(len(list)):
    if i % 2 == 1:
         res += list[i]
print(res)

# 3 вариант
list = [2, 3, 5, 9, 3]
res = 0
for i in range(1, len(list), 2):
    res += list[i]
print(res)

# 4 вариант
list = [2, 3, 5, 9, 3]
def sum_of_odd (input_list):
    res = 0
    for i in range(len(list)):
        if i % 2 == 1:
            res += list[i]
    return res

print (sum_of_odd(list))