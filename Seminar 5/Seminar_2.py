lst = [3, 5, 7, 10, 12]

def summ(x):
    return x + 2

res = list(map(lambda x: x + 2, lst))
res1 = list(map(int, lst))

print (res)
print (res1)
def more_five(x):
    if x > 5:
        return True

res2 = filter(more_five, res)
print(list(res2))

res4 = list(map(more_five, lst))
print(list(res4))

