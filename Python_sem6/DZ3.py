# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различные случайные варианты и выведите 4 успешных расстановки. *Выведите все успешные вариа нты расстановок
import DZ2 as dz
import random


BOARD_SIZE = 8
SIZE = 100


def rand(size):
    res = []
    i = 0
    while i < size:
        gen = [random.randint(0, size), random.randint(0, size)]
        i += 1
        if gen in res:
            i -= 1
        else:
            res.append(gen)
    return res

def my_func():
    count = 0
    count_tryes = 0
    while count < SIZE:
        count_tryes += 1
        t_qeen_list = rand(BOARD_SIZE)
        t = list(t_qeen_list)
        new_x, new_y = map(list, zip(*t_qeen_list))
        if dz.check(new_x, new_y):
            print(t_qeen_list, count_tryes)
            count += 1


if __name__ == '__main__':
    my_func()