def mult(x):
    #sleep(1)
    return x * 2


new_list_cmp1 = [mult(i) for i in range(5)]
#print(new_list_cmp1)# Формируется одноразово
new_list_cmp2 = (mult(i) for i in range(5))

for j in new_list_cmp1:
    print(j)

for k in new_list_cmp2:
    print(k)# Формируется по одному


for i, a in enumerate(new_list_cmp1):
    print(f'{i = }, {a = }')

for w in enumerate(new_list_cmp1):
    print(w)