#Реализуйте алгоритм перемешивания списка.
#1 вариант
import random

num = int(input("Введите число n, по которосу будет сформирован список от -n до n:"))
my_lst = list(range(-num, num, 2))
random.shuffle(my_lst)
print(my_lst)

