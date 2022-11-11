import time
from functools import wraps


def html_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        log_msg = '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Title</title></head><body>'
        log_msg += f"Комната: {', '.join(map(str, args))}\t"
        log_msg += f'Площадь комнаты: {res} м2 </p></body></html>'
        # with open('log_file2.html', 'w', encoding='utf-8') as fp:
        #     fp.write(log_msg)
        return res
    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        res = func(*args, **kwargs)
        finish = time.time_ns()
        print(finish - start)
        return res
    return wrapper

@html_decorator
@timer
def area_room4(x, y):
    """
    Фкнкция возвращает площадь комнаты
    :param x:
    :param y:
    :return:
    """
    return x * y

@timer
def cube(x, y, z):
    return x * y * z



def main():
    print(area_room4(5, 4))
    print(cube(3, 4, 5))
    # help(area_room3(3, 5))

if __name__ == '__main__':
    main()