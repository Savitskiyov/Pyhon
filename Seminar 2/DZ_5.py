#Реализуйте алгоритм перемешивания списка.
#1 вариант
# import random
#
# num = int(input("Введите число n, по которосу будет сформирован список от -n до n:"))
# my_lst = list(range(-num, num, 2))
# random.shuffle(my_lst)
# print(my_lst)
#
# #2 вариант
# num = int(input("Введите число n, по которосу будет сформирован список от -n до n:"))
# my_lst = list(range(-num, num+1))
# print(my_lst)
# my_lst.reverse()
# print(my_lst)

#3 вариант
import random

spisok = []

for i in range(0,21):
    spisok.append(random.randint(1,100))

def sort (array):
    res = []
    res2 = []
    for i in array:
        if i % 2 ==0:
            res.append(i)
        else:
            res2.append(i)
 #   res2.sort()
 #   res.sort()
    res.extend(res2)
    return res
print(spisok)
print (sort(spisok))


