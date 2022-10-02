#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

# 1 вариант

n = input("Введите число n:")
a = int(n.replace('.', ''))
print(a)
sum = 0
while (a != 0):
    sum = sum + a % 10
    a = a // 10
print(sum)

# 2 вариант
num = input("Введите число n:")
def sum_num(num):
    res = 0
    for i in num:
        if i == '.' or i == ',' or i == 'i':
            continue
        res += int(i)
    return res

print ( f'сумма чисел в числе {num} составляет {sum_num(num)}')

