# Задание на семинаре
# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

NUMBER = 100
SYSTEM_2 = 2
SYSTEM_8 = 8
def convert(number: int, system: int) -> list:
    temp = ''
    while number > 0:
        temp = temp + str(number % system)
        number = number // system
    # Разворот строки
    return temp[::-1]


def convert2(number: int, system: int) -> str:
    temp = list()
    while number > 0:
        temp.append(str(number % system))
        number = number // system
    # Разворот строки
    temp.reverse()
    return ''.join(temp)


print(f'Число Ob{NUMBER}, в двоичной системе {bin((NUMBER))}')
print(convert(NUMBER, SYSTEM_2))
print(convert2(NUMBER, SYSTEM_2))

print(f'Число 0o{NUMBER}, в восмиричной системе {oct((NUMBER))}')
print(convert(NUMBER, SYSTEM_8))
print(convert2(NUMBER, SYSTEM_8))