
def num_sequence(n):
    res_list = []
    sum_res = 0
    for i in range(1, n + 1):
        res = round((1 + 1 / i) ** i, 2)
        sum_res += res
        res_list.append(res)
    sum_res = round(sum_res, 2)
    return sum_res

#print((num_swquence(5)))