# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions

import fractions

numerator_1, denominator_1 = map(int, input('Введите числитель и знаменатель первой дроби, пример a/b: ').split("/"))
numerator_2, denominator_2 = map(int, input('Введите числитель и знаменатель второй дроби, пример a/b: ').split("/"))

d1 = numerator_1 * numerator_2
d2 = denominator_1 * denominator_2
g1 = numerator_1 * denominator_2 + numerator_2 * denominator_1
g2 = denominator_1 * denominator_2

#print(d1, d2, g1, g2 )

def gcd_loop(a, b):
    if a > b:
        temp = b
    else:
        temp = a
    for i in range(1, temp + 1):
        if(a % i == 0) and (b % i == 0):
            gcd = i
    return gcd


gcd_work = gcd_loop(d1, d2)
gcd_sum = gcd_loop(g1, g2)
#print(gcd_work,gcd_sum)
print(f'Произведение дробей равно: {int(d1/gcd_work)}/{int(d2/gcd_work)}')
print(f'Сумма дробей равна: {int(g1/gcd_sum)}/{int(g2/gcd_sum)}')

f1 = fractions.Fraction(numerator_1, denominator_1)
f2 = fractions.Fraction(numerator_2, denominator_2)
print(f"{f1 * f2} fractions *")
print(f"{f1 + f2} fractions +")