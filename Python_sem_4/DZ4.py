# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

num = [52, 19, 12, 7323, 8, 15, 1, 2, 3, 4, 5]

index_1 = int(input('Введите первый индекс: '))
index_2 = int(input('Введите второй индекс: '))
def my_func(mas , first, second):
    if index_1 <= index_2:
        index = 0 if first < 0 else first
        s = sum(mas[index:second+1])  # взять сумму между индексами
        return s
    else:
        index = 0 if first < 0 else first
        s = sum(mas[second:index+1])  # взять сумму между индексами
        return s


print(my_func(num, index_1, index_2))
