# Задача на семинаре
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

cort = ("Hello", 2, True, 3.14, "world", 6.14, 4, 5, False)
dic = {}
dic1 = {}
dic2 = {}
for i in cort:
    res = type(i)
    if res in dic:
        dic[res].append(i)
    else:
        dic[res] = [i]

for item in cort:
    dic1.setdefault(type(item), []).append(item)
    dic2[type(item)] = dic2.get(type(item), []) + [item]


print(dic)
print(dic1)
print(dic2)
