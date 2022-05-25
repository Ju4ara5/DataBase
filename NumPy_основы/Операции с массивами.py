import numpy as np

arr = np.arange(1, 11)  # [ 1  2  3  4  5  6  7  8  9 10]

arr + arr  # [ 2  4  6  8 10 12 14 16 18 20]  то же: (arr * 2)
arr - arr  # [0 0 0 0 0 0 0 0 0 0]
arr + 5  # [ 6  7  8  9 10 11 12 13 14 15]
arr - 5   # [-4 -3 -2 -1  0  1  2  3  4  5]

arr * arr  # [  1   4   9  16  25  36  49  64  81 100]
arr / arr  # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
list(arr / 2)  # [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
arr ** 3  # [   1    8   27   64  125  216  343  512  729 1000]

np.sqrt(arr)  # квадратный корень элементов
np.exp(arr)  # экспоненты элементов
np.max(arr)  # максимальный элемент (arr.max) (np.min минимальный)
np.cos(arr)  # cos элементов ... и так далее (в нэте универсальные функции numpy)


'''Деление на 0 в numpy:'''
# RuntimeWarning: divide by zero encountered in true_divide
arr / 0  # [inf inf inf inf inf inf inf inf inf inf] бесконечность
arr2 = np.arange(0, 11)  # создаём массив с 0
arr2 / 0  # [nan inf inf inf inf inf inf inf inf inf inf]  nan - not a number
arr2 / arr2  # [nan  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]
