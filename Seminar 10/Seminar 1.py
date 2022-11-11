def my_func(x, y):
    print(f'{x = }')
    print(f'{y = }')
    return x * y

# print(my_func(5, 3))


def my_func2(x, y, *args):
    print(f'{x = }')
    print(f'{y = }')
    other = args
    print(f'{other = }')


# my_func2(5, 4, 15, 35, 12)
#
# print('dsfdfsdf', 'dsfsdfsdfds', 'dsfdsfsdf', sep='//', end='  ')

# * или / делит на именновые и позиционные параметры
def my_func3(x, y, *, a, b, c):
    print(f'{x = }')
    print(f'{y = }')
    print(f'{a = }')
    print(f'{b = }')
    print(f'{c = }')


# f = '15'
# my_func3(5, f, a=4, b=f, c=6)

def my_func4(*args, **kwargs):
    a, b, *c = args
    d = kwargs
    print(f'{a = }')
    print(f'{b = }')
    print(f'{c = }')
    print(f'{d = }')


my_func4(1, 2, 3, 4, 5, z=12, g=45)
