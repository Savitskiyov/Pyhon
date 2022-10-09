# 2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# 1 вариант
lst = [2, 3, 4, 5, 6, 7]
#lst = list(map(int, input("Введите числа через запятую:").split(',')))
l = len(lst)

if l % 2 != 0:
    temp = l//2 + 1
else:
    temp = l//2

my_list =[]
for i in range(temp):
    y = lst[i] * lst[l-i-1]
    my_list.append(y)

print(my_list)


# 2 вариант
lst = list(map(int, input("Введите числа через запятую:").split(',')))
lst = [2, 3, 4, 5, 6, 7]
def mult_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)


mult_lst(lst)