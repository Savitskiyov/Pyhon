# Декораторы
import datetime
from functools import wraps


def decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'Площадь комнаты: {res} м2')
        return func(*args, **kwargs)
    return wrapper


@decorator
def area_room(x, y):
    return x * y


print(area_room(5, 4))


def decorator2(func):
    def wrapper(*args, **kwargs):
        a, b = args
        per = 2 * (a + b)
        print(f'Периметр комнаты: {per} ')
        return func(*args, **kwargs)
    return wrapper


@decorator2
def area_room2(x, y):
    return x * y


print(area_room2(5, 4))


def decorator3(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        wraps docs
        :param x:
        :param y:
        :return:
        """
        log_msg = f"{datetime.datetime.now(): %d.%m.%Y %H:%M:%S} "
        log_msg += f"функция: {func.__name__}\t"
        log_msg += f"параметры: {', '.join(map(str, args))}\t"
        res = func(*args, **kwargs)
        log_msg += f'результат: {res}\n'
        print(log_msg)
        with open('log_file.log', 'a', encoding='utf-8') as fp:
            fp.write(log_msg)
        return func(*args, **kwargs)
    return wrapper


@decorator3
def area_room3(x, y):
    """
    Фкнкция возвращает площадь комнаты
    :param x:
    :param y:
    :return:
    """
    return x * y


def main():
    print(area_room3(5, 4))
    print(area_room3.__doc__)
    # help(area_room3(3, 5))

if __name__ == '__main__':
    main()



def html_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        log_msg = '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Title</title></head><body>'
        log_msg += f"Комната: {', '.join(map(str, args))}\t"
        log_msg += f'Площадь комнаты: {res} м2 </p></body></html>'
        with open('log_file.html', 'w', encoding='utf-8') as fp:
            fp.write(log_msg)
        return res
    return wrapper


@html_decorator
def area_room4(x, y):
    """
    Фкнкция возвращает площадь комнаты
    :param x:
    :param y:
    :return:
    """
    return x * y


def main():
    print(area_room4(5, 4))
    print(area_room4.__doc__)
    # help(area_room3(3, 5))

if __name__ == '__main__':
    main()