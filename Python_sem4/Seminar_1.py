# ✔ Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

import re

#val = input('Введите предложение :')
val ='Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.'
def my_func (text):
    my_list = sorted(re.sub(r'\W', ' ', text).split())
    max_len = len(max(my_list, key=len))
    for num, val in enumerate(my_list, start=1):
        print(f'{num} {val:>{max_len}}')
        # if len(val) < len(max_len):
        #     val2 = " " * int(len(max_len)-len(val)) + val
        #     print(f'{num} {val2}')
        # else:
        #     print(f'{num} {val}')

my_func(val)