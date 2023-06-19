# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

# *args
# hash

def my_func (**kwargs):
    for _ in kwargs:
        kwargs = dict(reversed(item) for item in kwargs.items())
        return kwargs

def my_func2 (**kwargs):
    for _ in kwargs:
        kwargs2 = {v: k for k, v in kwargs.items()}
        return kwargs2

print(my_func(a = 0, b =1, c = 3, d = 4))
print(my_func2(a = 0, b =1, c = 3, d = 4))

