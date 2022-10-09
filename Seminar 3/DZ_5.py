#5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи] (https://ru.wikipedia.org/wiki/Негафибоначчи)

# 1 вариант
import itertools

my_list = []
my_list2 = []
num = int(input("Введите число:"))

def fib(n):
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

for i in range(num + 1):
    my_list.append(fib(i))


for ind, element in enumerate(my_list, start=0):
    if ind % 2 == 1:
        my_list2.append(element)
    else:
        my_list2.append(element*-1)

res = list(itertools.chain(reversed(my_list2), my_list[1:])) # Объединенисе строк
print(res)


# 2 вариант
def nega_fibonacci(n):
    list_negafibonacci = []
    for i in range(1 , n + 1):
        fibo_i = fib(i)
        list_negafibonacci.append(fibo_i)
        if i != 1:
            list_negafibonacci.insert(0, (-1) ** (i) * fibo_i)
    print(f'Негафибоначчи: {list_negafibonacci}')

print (nega_fibonacci(10))