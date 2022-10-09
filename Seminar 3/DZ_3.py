# 3.Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# lst = [1.1, 1.2, 3.1, 5, 10.01]

# 1 вариант
# #lst = [1.1, 1.2, 3.1, 5, 10.01]
lst = list(map(float, input("Введите числа через запятую:").split(',')))
my_list = []

for index, element in enumerate(lst, start=0):
    if element % 1 != 0:
        my_list.append(round(element % 1, 2))
        index += 1

print(max(my_list)-min(my_list))


# 2 вариант
lst = list(map(float, input("Введите числа через запятую:").split(',')))
new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
print(max(new_lst) - min(new_lst))