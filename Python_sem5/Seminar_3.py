# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.
LIMIT = 5

text = set(input('Введите текст: '))
my_func = {val: ord(val) for val in text}
my_func2 = iter(my_func.items())
print(my_func)

for _ in range(LIMIT):
    print(next(my_func2))
