# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте список по убыванию суммы цифр

num = [52, 19, 12, 7323, 8, 15]

def get_sum(nu: int):
    return sum(map(int, str(nu)))

def get_dict (lst: list):
    return dict(sorted(zip(map(get_sum, lst), lst)))

print(get_dict(num))
print(sorted(num, key=get_sum))
