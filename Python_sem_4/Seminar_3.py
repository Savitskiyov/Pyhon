# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

data = input('ВВедите значения через пробел: ')

def my_func (data):
    num_1, num_2 = map(int, data.split())
    print(num_1, num_2)
    dict_num ={}
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1
    for elem in range(num_1, num_2+1):
        dict_num[chr(elem)] = elem
    return dict_num



print(my_func(data))