#2.Для натурального n создать список, состоящий из элементов последовательности 3n + 1
#Пример:
#- Для n = 6: [4, 7, 10, 13, 16, 19]

n = int(input("Введите вещественное число n:"))
result = []
sign = 4
for i in range(0 , n):
    result = sign
    sign = sign + 3
    print(result, end=',')

#2 вариант
n = int(input("Введите вещественное число n:"))
result = []
for i in range(1 , n+1):
    result.append(3*i + 1)
print(*result)