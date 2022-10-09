# 5.Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random

k_1 = int(input("Введите натуральную степень для первого файла k = "))
k_2 = int(input("Введите натуральную степень для второго файла k = "))

# Функция рандома от 0 до 100
def rand():
    return random.randint(1, 100)


# Сформировать случайным образом список коэффициентов (значения от 0 до 100) для двух списков
my_list = list(rand() for i in range(k_1+1))
my_list2 = list(rand() for i in range(k_2+1))

# Функция записи многочлена из 4 д.з
def func(val):
    wr = ''
    # если степень меньше 1
    if len(val) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(val)):
        # степень от k3
            if i != len(val) - 1 and i != len(val) - 2:
                wr += f'{val[i]}x^{len(val) - i - 1} + '
        # степень от k2
            elif i == len(val) - 2:
                wr += f'{val[i]}x + '
        # степень от k1
            elif i == len(val) - 1:
                wr += f'{val[i]} = 0'

    return wr

# запись многочлена в файл
def wr_def(val1, val2):
    with open(val1, 'w') as data:
        data.write(val2)

# Создания файлов
file1 = 'DZ_5_1.txt'
file2 = 'DZ_5_2.txt'
file3 = 'DZ_5_3.txt'

wr_def(file1, func(my_list))
wr_def(file2, func(my_list2))

# возвращает строку многочлен
def get_pol(file_name):
    with open(file_name, 'r') as data:
        mng1 = data.readlines()
    return mng1

# Запись множеств в переменные
str1 = list(get_pol(file1))
str2 = list(get_pol(file2))

# получение степени многочлена
def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# получение коэффицента члена многочлена
def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        koeff = int(k[:i])
    return koeff


# разбор многочлена и получение его коэффициентов
def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1  # степень
    ii = l - 1  # индекс
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1

    return lst

# нахождение суммы многочлена
lst1 = calc_mn(str1)
lst2 = calc_mn(str2)

# если разные длины списков, то короткий список расширяем нулями
lst1.extend([0,] * (len(lst2) - len(lst1)))
lst2.extend([0,] * (len(lst1) - len(lst2)))

# нахождение суммы многочлена
sum_mn = list(map(sum, zip(lst1, lst2)))
reverse_sum = list(reversed(sum_mn))


wr_def(file3, func(reverse_sum))
str3 = list(get_pol(file3))

print(f"Первый многочлен {str1}")
print(f"Второй многочлен {str2}")
print(f"Результирующий многочлен {str3}")



