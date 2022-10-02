# Рекурсия
def fib(n):
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

number = 8
for i in range(number +1):
    print(fib(i))