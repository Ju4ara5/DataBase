import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4],
                   'B': [123, 245, 321, 123],
                   'C': ['aaa', 'bbb', 'ccc', 'ddd']})

#        A    B    C
#     0  1  123  aaa
#     1  2  245  bbb
#     2  3  321  ccc
#     3  4  123  ddd

df['A'].sum()  # 10
df['B'].sum()  # 812
df['C'].sum()  # aaabbbcccddd

'ищим уникальные значения'
'в столбце B'
df['B'].unique()  # [123 245 321]

'количество уникальных значений в столбце B'
len(df['B'].unique())  # 3
df['B'].nunique()  # 3

'количество повторений значений в столбце B'
df['B'].value_counts()
#     123    2
#     245    1
#     321    1
#     Name: B, dtype: int64

'Выборка:'
'все строки из df где значения в столбце A < 3'
df[df['A'] < 3]
#        A    B    C
#     0  1  123  aaa
#     1  2  245  bbb
'все строки из df где значения в столбце A < 3 и {(& - and, | - or)} B < 200'
df[(df['A'] < 3) & (df['B'] < 200)]
#        A    B    C
#     0  1  123  aaa

'APPLY(): (применить)'
def times3(x):
    return x * 3


df['A'].apply(times3)  # или:
df['A'].apply(lambda x: x * 3)
#     0     3
#     1     6
#     2     9
#     3    12
#     Name: A, dtype: int64

df['A'].apply(times3).sum()  # 30
df['A'].apply(lambda x: x * 3).sum()  # 30

'длина каждого элемента в столбце С'
df['C'].apply(len)
#     0    3
#     1    3
#     2    3
#     3    3
#     Name: C, dtype: int64

'получаем имена столбцов'
df.columns  # Index(['A', 'B', 'C'], dtype='object')
'получаем индексы'
df.index  # RangeIndex(start=0, stop=4, step=1)

'Сортировка и упорядочивание'
'по столбцу B'
df.sort_values('B')
#        A    B    C
#     0  1  123  aaa
#     3  4  123  ddd
#     1  2  245  bbb
#     2  3  321  ccc

df.isnull()
#            A      B      C
#     0  False  False  False
#     1  False  False  False
#     2  False  False  False
#     3  False  False  False


'pivot_table():'
df2 = pd.DataFrame({'A': [1, 1, 1, 2, 2, 2],
                    'B': [123, 222, 222, 123, 123, 222],
                    'C': ['aaa', 'bbb', 'aaa', 'bbb', 'bbb', 'aaa'],
                    'D': [1, 2, 4, 3,  1, 5]})

#        A    B    C  D
#     0  1  123  aaa  1
#     1  1  222  bbb  2
#     2  1  222  aaa  4
#     3  2  123  bbb  3
#     4  2  123  bbb  1
#     5  2  222  aaa  5

df2.pivot_table(values='D', index=['A', 'B'], columns=['C'])
#     C      aaa  bbb
#     A B
#     1 123  1.0  NaN
#       222  4.0  2.0
#     2 123  NaN  2.0
#       222  5.0  NaN
