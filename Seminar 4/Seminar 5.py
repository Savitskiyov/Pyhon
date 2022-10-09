list1 = [1, 2, 3, 5, 8, 15, 23, 38]

def mylt (n):
    return n ** 2

my_list =[(i, mylt(i)) for i in list1 if i % 2 == 0]
print(my_list)