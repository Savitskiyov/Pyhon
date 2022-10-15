from pprint import pprint

def mystr():
    return '555'

def nest():
    return [2, 4, 8, 10]


my_dict = {
    'name': 'Sasha',
    'age': 29,
    mystr(): nest()
           }

print(my_dict)

my_dict2 = {
    'name': 'Sasha',
    'age': 29,
    'last_name': 'Sergeev',
    'city': 'Yesk',
    'status': 'married',
           }

print(my_dict2)

pprint(my_dict2)

print('Имя: ', my_dict2['name'])
print('Возраст: ', my_dict2['age'])
my_dict2['age'] = 30
print('Возраст: ', my_dict2.get('age'))
print('Есть машина: ', my_dict2.get('is_car')) # get не выдает ошибку
print('Есть машина: ', my_dict2.get('is_car', False)) # False - выводится если нет в словаре
print('Возраст: ', my_dict2.get('age'))
my_dict2.setdefault('is_car', True) # Запишет новое значение в словарь
pprint(my_dict2)

my_dict3 = {
    'name': 'Pasha',
    'age': 22,
    'last_name': 'Derbeev',
    'city': 'Tomsk',
    'hight': 185,
           }

pprint(my_dict3)
print()
my_dict3.update(my_dict2) # объединяем ключи двух словарей
pprint(my_dict2)

for i in my_dict2:
    print(i)

for i in my_dict2.keys():
    print(i)

for i in my_dict2.values():
    print(i)

for i in my_dict2.values():
    print(i, my_dict2[i])

for k, v in my_dict3.items():
    print(k, v)
