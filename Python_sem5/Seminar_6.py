# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило: «число является простым, если делится нацело только на единицу и на себя».

def prime(n):
    for i in range(2, int((n ** 0.5) + 1)):
        if n % i == 0:
            return False
        return True


def gen_num(num):
    for i in range(2, num):
        if prime(i):
            yield i

a = gen_num(int(input('Введите число: ')))
print(*a)