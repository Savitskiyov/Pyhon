# Напишите функцию для транспонирования матрицы
import numpy as np
matrix = [[1, 2], [31, 4], [17, 15], [20, 48]]

def my_func (mat):
    zip_matrix = zip(*mat)
    transpon_matrix = [list(row) for row in zip_matrix]
    return transpon_matrix

def my_func2 (mat):
    arr_matrix = np.array(mat)
    transpon_matrix2 = arr_matrix.transpose()
    return transpon_matrix2

print(matrix)
print(my_func(matrix))
print(my_func2(matrix))
