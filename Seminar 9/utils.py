def division (a, b):
    return a / b

try:
    print(division(10, 'd'))
except ZeroDivisionError:
    print('на ноль делить нельзя')
except TypeError:
    print('Введите число')
