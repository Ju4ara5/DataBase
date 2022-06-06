import numpy as np
import pandas as pd

dict1 = {'Company': ['COMP1', 'COMP1', 'COMP2', 'COMP2', 'COMP3', 'COMP3'],
         'Months': ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN'],
         'Salary': [2000, 1500, 3000, 5000, 2500, 3500]}

df = pd.DataFrame(dict1)
#      Company Months  Salary
#    0   COMP1    JAN    2000
#    1   COMP1    FEB    1500
#    2   COMP2    MAR    3000
#    3   COMP2    APR    5000
#    4   COMP3    MAY    2500
#    5   COMP3    JUN    3500


'групируем df по столбцу Company'
df.groupby('Company')
#  <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000022B688A0D30>
'получаем среднее значение Salary (по группе Company) для каждой COMP'
df.groupby('Company').mean()
'''отсуствует столбец Months 
   т.к. pandas не может вычислить среднее арифметическое из строк
    по этому игнорирует этот столбец'''
#               Salary
#      Company
#      COMP1    1750.0        (2000+1500)/2
#      COMP2    4000.0        ...
#      COMP3    3000.0        ...

'2 метод. через переменные:'
groupby_company = df.groupby('Company')
groupby_company.mean()        # результат тот же
'так же сумма:'
groupby_company.sum()
#            Salary
#   Company
#   COMP1      3500
#   COMP2      8000
#   COMP3      6000
'среднеквадротичное отклонение:'
groupby_company.std()
#                 Salary
#   Company
#   COMP1     353.553391
#   COMP2    1414.213562
#   COMP3     707.106781
'максимальное значание'
df.groupby('Company').max()
#           Months  Salary
#   Company
#   COMP1      JAN    2000
#   COMP2      MAR    5000
#   COMP3      MAY    3500


'метод описания'
df.groupby('Company').describe()
#            Salary
#             count    mean          std     min     25%     50%     75%     max
#    Company
#    COMP1      2.0  1750.0   353.553391  1500.0  1625.0  1750.0  1875.0  2000.0
#    COMP2      2.0  4000.0  1414.213562  3000.0  3500.0  4000.0  4500.0  5000.0
#    COMP3      2.0  3000.0   707.106781  2500.0  2750.0  3000.0  3250.0  3500.0
'разворачиваем наоборот:'
df.groupby('Company').describe().transpose()
#    Company             COMP1        COMP2        COMP3
#    Salary count     2.000000     2.000000     2.000000
#           mean   1750.000000  4000.000000  3000.000000
#           std     353.553391  1414.213562   707.106781
#           min    1500.000000  3000.000000  2500.000000
#           25%    1625.000000  3500.000000  2750.000000
#           50%    1750.000000  4000.000000  3000.000000
#           75%    1875.000000  4500.000000  3250.000000
#           max    2000.000000  5000.000000  3500.000000

comp_2 = df.groupby('Company').describe().transpose()['COMP2']
#  Salary  count       2.000000
#          mean     4000.000000
#          std      1414.213562
#          min      3000.000000
#          25%      3500.000000
#          50%      4000.000000
#          75%      4500.000000
#          max      5000.000000
#  Name: COMP2, dtype: float64


type(comp_2)  # pandas.core.series.Series
type(groupby_company.sum())  # pandas.core.frame.DataFrame

'можем получить какое-то определённое значение для какойто компании'
groupby_company.sum().loc['COMP3']
'или'
df.groupby('Company').sum().loc['COMP3']
#  Salary    6000
#  Name: COMP3, dtype: int64

'можно посчитать количество объектов'
df.groupby('Company').count()
#            Months  Salary
#   Company
#   COMP1         2       2
#   COMP2         2       2
#   COMP3         2       2

df.count()
#  Company    6
#  Months     6
#  Salary     6
#  dtype: int64
