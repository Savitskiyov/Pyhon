# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]
#
# seq(3)
# seq(8)
# seq(100)
# seq(8)
# seq(3)
# seq(100)

# def <конструктор декоратора>(<параметры декоратора>):
#
#     def <декоратор>(<декорируемая ф-ция>):
#         def <обёртка>(*args):
#             res = <декорируемая ф-ция>(*args)
#             return res
#         return <обёртка>
#
#     return <декоратор>

# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами,
# CДЕЛАНО В ПРЕДЫДУЩЕМ ДОМАШНЕМ ЗАДАНИИ
import datetime
import time
# def log_func(log_lvl=0):

def log_func(log_lvl=0):
    def logger2(func):
        def wrapper(*args, **kwargs):
            if log_lvl >= 1:
                log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
                log_msg += f'Функция: {func.__name__}\t'
                res = func(*args, **kwargs)
                log_msg += f'Результат: {res}\n'
            else:
                res = func(*args, **kwargs)
                log_msg: str = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\n'
            with open('DZ_log.log', 'a', encoding='utf-8') as fp:
                fp.write(log_msg)
            return res

        return wrapper

    return logger2


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        res = func(*args, **kwargs)
        finish = time.time_ns()
        print(finish - start)
        return res
    return wrapper


def cacher(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = args
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


@log_func(1)
@timer
@cacher
def seq(num):
    my_list = []
    for i in range(1, num+1):
        res = (1 + i) ** i
        my_list.append(res)
        i += 1
    return my_list

print(seq(10))
print(seq(3))
print(seq(8))
print(seq(100))
print(seq(8))
print(seq(100))
print(seq(3))
print(seq(4))


