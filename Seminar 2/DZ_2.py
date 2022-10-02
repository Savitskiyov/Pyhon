# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# 1 вариант
n = int(input("Введите число n:"))
result = 1
for i in range(1, n + 1):
    result = result * i
    print(result, end=' ')

# 2 вариант
n = int(input("Введите число n:"))
def list_numbers(num):
    res = 1
    multi = []
    for n in range(1, num+1):
        res *= n
        multi.append(res)
    return multi

print (list_numbers(n))