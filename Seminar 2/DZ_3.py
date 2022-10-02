#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.


# 1 вариант
num = int(input("Введите число n:"))

my_str = list()
for i in range(1, num+1):
    my_str.append((1 + 1/i)**i)

print(sum(my_str))

# 2 вариант
num = int(input("Введите число n:"))

def list_numbers(num):
    my_str= []
    for i in range(1, num + 1):
        form = (1 + 1/i)**i
        my_str.append(form)
    return my_str

print(sum(list_numbers(num)))
