# вывод уникальных значений
# my_list = [1, 1, 2, 3, 4, 5, 1, 3, 4, 5]
# print(set(my_list))


my_list = list(map(int, input("Введите числа через пробел:").split(' ')))
my_list2 =[]

for i, element in enumerate(my_list):
    if my_list.count(element) == 1:
        my_list2.append(element)

my_list3 = list(element for i, element in enumerate(my_list) if my_list.count(element) == 1)

print(my_list2)
print(my_list3)
