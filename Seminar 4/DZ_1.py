# 1.Вычислить число c заданной точностью d
# *Пример:*
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

d = input("Введите число c заданной точностью d:")

def my_func (d1):
    if d1.find('.') != -1:
        acc = d.split('.')
        acc = len(acc[1])
    elif d1.find(',') != -1:
        acc = d.split('.')
        acc = len(acc[1])
    else:
        acc = 0
    print(f'Число π c точность {d} = {round(math.pi, acc)}')


print(math.pi)
my_func(d)
