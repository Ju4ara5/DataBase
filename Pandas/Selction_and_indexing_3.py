import numpy as np
import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(4, 3),
                  ['a', 'b', 'c', 'd'],
                  ['X', 'Y', 'Z'])
# рандомный результат:
#           X         Y         Z
# a  0.171855 -0.443628 -0.725869
# b -1.155239  0.440830 -1.689575
# c -0.624729 -1.338557  0.578933
# d -0.678096  0.161559 -1.384594

'''Все результаты что будут ниже будут рандомными 
   и не будут соответствовать таблице DataFrame выше,
   т.к. при каждом новом запуске кода, генерируется новая DataFrame'''

'сравнение с 0 значений DataFrame'
bool_df = df > 0
# Результат:
#        X      Y      Z
# a  False   True   True
# b   True   True  False
# c   True   True   True
# d   True  False  False

'Условная выборка'
df[bool_df]  # или df[df > 0] чтоб не создавать переменную
# как результат в место False NaN
#           X         Y         Z
# a       NaN       NaN  1.106889
# b       NaN  0.270582       NaN
# c  0.938411  0.868320       NaN
# d  1.322695  1.870152  0.612884

df['Y'] > 0
# результат:
# a    False
# b    False
# c     True
# d     True
# Name: Y, dtype: bool

'Вернет ряды в которых значение в столбце Y > 0'
df[df['Y'] > 0]
#           X         Y         Z
# b  0.902430  0.422324  0.594583
# d -1.507742  0.011399  1.715757



'Все ряды DataFrame где X < 0'
df_X_min_0 = df[df['X'] < 0]
#           X         Y         Z
# b -0.026266  0.331150 -2.315148
# c -2.042473 -0.235459  0.267703
# d -0.447277  0.900725 -0.339758
'''Из исходной DataFrame, выше были выделены все ряды где 'X' < 0 (df_X_min_0),
   и получаем все значения 'Z' из df_X_min_0'''
df_X_min_0['Z']
# b   -2.315148
# c    0.267703
# d   -0.339758
# Name: Z, dtype: float64
'более короткий вариант без создания переменных'
df[df['X'] < 0]['Z']
# b   -2.315148
# c    0.267703
# d   -0.339758
# Name: Z, dtype: float64
'также можно вызвать 2 столбца, на пример Z и Y'
df[df['X'] < 0][['Z', 'Y']]



'Далее рассмотрим использование множественных условий'
'Передаем несколько условиий и получаем значения из них'
"Выбираем все строки где значания 'X'>0 и(&) 'Z'<0:"
# в место and используем & !
df[(df['X'] > 0) & (df['Z'] < 0)]
# результат:
#           X         Y         Z
# c  0.225849  0.619730 -0.972494
# d  0.329004 -0.448065 -1.532916

"Выбираем все строки где значания 'X'>0 или(|) 'Z'<0:"
# в место or используем | !
df[(df['X'] > 0) | (df['Z'] < 0)]
# результат:
#           X         Y         Z
# a  1.393201  1.008906 -0.216687
# c -0.523332  0.308078 -1.184116
# d  0.146212  0.016894 -3.019158


'Переустанавливаем индексы'
df.reset_index()  # без сохранения, для просмотра. чтоб сохранить df.reset_index(inplace=True)
#   index         X         Y         Z
# 0     a  0.209524 -0.852603 -2.824563
# 1     b -0.249389  0.706996  0.745796
# 2     c -0.985523 -0.027289  0.572313
# 3     d  0.723670 -1.019722 -0.975921

'Добавляем столбец'
new = [5, 13, 45, 0]
df['NEW'] = new
#           X         Y         Z  NEW
# a  0.114698 -0.374026  1.173682    5
# b -0.251772  0.223520 -1.270430   13
# c  1.620681  0.151429 -0.045597   45
# d  0.266874  2.141524  0.034185    0

'Можем указать любой столбец DataFrame как индексы для этой DataFrame'
df.set_index('NEW')  # чтоб сохранить это изменение: df.set_index('NEW', inplace=True)
#             X         Y         Z
# NEW
# 5    0.013663 -0.095930  0.948646
# 13  -0.014297  0.076389 -0.613992
# 45  -1.442643 -0.672146  1.127003
# 0    0.146315 -0.069547  0.724834
