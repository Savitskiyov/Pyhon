# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
import sys
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
COUNT = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)

print(num)
while True:
    numb = int(input("Введите число от 0 до 10: "))
    if numb > UPPER_LIMIT:
        print(f"Вы ввели число {numb}, которое больше заданного диапазона от {LOWER_LIMIT} до {UPPER_LIMIT} ")
        COUNT -= 1
        print(f"Оталось попыток {COUNT}")
    if numb < LOWER_LIMIT:
        print(f"Вы ввели число {numb}, которое меньше заданного диапазона от {LOWER_LIMIT} до {UPPER_LIMIT}")
        COUNT -= 1
        print(f"Оталось попыток {COUNT}")
    elif num == numb:
        if COUNT == 10:
            print(f"Вы угадил число {num} за 1 попытку")
            sys.exit()
        else:
            print(f"Вы угадил число {num} за {10-COUNT+1} попыток")
            sys.exit()
    elif num > numb:
        COUNT -= 1
        print(f"Ваше число {numb} меньше искомого значения, осталось попыток {COUNT}")
    elif num < numb:
        COUNT -= 1
        print(f"Ваше число {numb} больше искомого значения, осталось попыток {COUNT}")



