# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions

a, b = map(int, input('Введите числитель и знаменатель первой дроби, через пробел: ').split())
c, d = map(int, input('Введите числитель и знаменатель второй дроби, через пробел: ').split())


print(a, b, c, d)
print(f'Сумма дробей равна {(a / b) + (c / d)}')
print(f'Произведение дробей равно {(a / b) * (c / d)}')
# Проверка
print(fractions.Fraction(a, b) + fractions.Fraction(c, d))
print(fractions.Fraction(a, b) * fractions.Fraction(c, d))
# print(second)