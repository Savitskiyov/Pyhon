# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input("Введите натуральную степень k = "))

# Функция рандома от 0 до 100
def rand():
    return random.randint(1, 100)


# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
my_list = list(rand() for i in range( k+1))


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

def wr_def(val2):
    with open('DZ_4.txt', 'w') as data:
        data.write(val2)



print(func(my_list))
wr_def(func(my_list))
#print(my_list)
