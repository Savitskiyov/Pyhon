# Создайте функцию генератор чисел Фибоначчи https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
def fibo(number):
    fibo_list = [0, 1]
    current_number = 0
    while current_number < number:
        while len(fibo_list) < number:
            fibo_list.append(sum(fibo_list[-2:]))
        yield fibo_list[current_number]
        current_number += 1

print(*fibo(10))