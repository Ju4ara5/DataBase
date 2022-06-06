import numpy as np
import pandas as pd

dict1 = {'one': [10, np.nan, 30],
         'two': [np.nan, np.nan, 50],
         'three': [10, 10, 10]}

df = pd.DataFrame(dict1)
#     one   two  three
# 0  10.0   NaN     10
# 1   NaN   NaN     10
# 2  30.0  50.0     10

'удаляем все строки в которых есть NaN'
df.dropna()
#     one   two  three
# 2  30.0  50.0     10

'удаляем все столбцы в которых есть NaN'
df.dropna(axis=1)
#    three
# 0     10
# 1     10
# 2     10

'удаляем все строки с NaN значениями кроме тех в которых есть хотябы 2 не NaN значения'
df.dropna(thresh=2)
#      one   two  three
#  0  10.0   NaN     10
#  2  30.0  50.0     10

'заменяем NaN значения другими значениями'
df.fillna(value='Something')
#          one        two  three
# 0       10.0  Something     10
# 1  Something  Something     10
# 2       30.0       50.0     10

'в место NaN помещаем среднее значение всех значений one столбца'
'можно ище: сумму(sum), максимальное(max)... и все что есть в math'
df['one'].fillna(value=df['one'].mean())
# 0    10.0
# 1    20.0  - среднее(mean) "(10+30)/2"
# 2    30.0
# Name: one, dtype: float64
