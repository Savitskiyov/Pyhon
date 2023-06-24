# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
import sys
from random import randint

L_LIMIT = 0
U_LIMIT = 100
COUNT = 10


def my_func(LOWER_LIMIT, UPPER_LIMIT, count):
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    while True:
        numb = int(input(f"Введите число от {L_LIMIT} до {U_LIMIT}: "))
        if count == 0:
            print(f"Кол-во попыток исчерпано")
        elif numb > UPPER_LIMIT:
            print(f"Вы ввели число {numb}, которое больше заданного диапазона от {LOWER_LIMIT} до {UPPER_LIMIT} ")
            count -= 1
            print(f"Оталось попыток {count}")
        elif numb < LOWER_LIMIT:
            print(f"Вы ввели число {numb}, которое меньше заданного диапазона от {LOWER_LIMIT} до {UPPER_LIMIT}")
            count -= 1
            print(f"Оталось попыток {count}")
        elif num == numb:
            if count == 10:
                print(f"Вы угадил число {num} за 1 попытку")
                sys.exit()
            else:
                print(f"Вы угадил число {num} за {10-count+1} попыток")
                sys.exit()
        elif num > numb:
            count -= 1
            print(f"Ваше число {numb} меньше искомого значения, осталось попыток {count}")
        elif num < numb:
            count -= 1
            print(f"Ваше число {numb} больше искомого значения, осталось попыток {count}")



print(my_func(L_LIMIT,U_LIMIT,COUNT))