# Улучшаем задачу 1.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
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

if "__main__" == __name__:
    _, L_LIMIT, U_LIMIT, COUNT = sys.argv
    print(my_func(int(L_LIMIT), int(U_LIMIT), int(COUNT)))