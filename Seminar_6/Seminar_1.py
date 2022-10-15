from random import randint
from time import sleep


def more_five(x):
    if x > 5:
        return True

new = [2, 5, 10 ,12, 15, 1 ,2]

res_map = map(more_five, new)
print(list(res_map))


list_cmp = [randint(0, 10) for i in range(10) if i % 2 == 0]
#print(list_cmp)

set_cmp = [randint(0, 10) for i in range(10)]
#print(set_cmp)

dict_cmp = {str(i): randint(0, 10) for i in range(10)}
#print(dict_cmp)

x = [1, 2, 3, 24]
#print(id(x))
x.append(17)
#print(id(x))

new_list_cmp = (randint(0, 10) for i in range(10) if i % 2 == 0)

# print(new_list_cmp.__next__())
# print(new_list_cmp.__next__())
# print(new_list_cmp.__next__())
# print(list(new_list_cmp)) # генерирует 1 раз
# print(list(new_list_cmp))
#



