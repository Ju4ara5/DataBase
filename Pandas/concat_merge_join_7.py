import pandas as pd

'concat():'

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

'результат'
'df1'
#          A   B   C   D
#      0  A0  B0  C0  D0
#      1  A1  B1  C1  D1
#      2  A2  B2  C2  D2
#      3  A3  B3  C3  D3
'df2'
#          A   B   C   D
#      4  A4  B4  C4  D4
#      5  A5  B5  C5  D5
#      6  A6  B6  C6  D6
#      7  A7  B7  C7  D7
'df3'
#            A    B    C    D
#      8    A8   B8   C8   D8
#      9    A9   B9   C9   D9
#      10  A10  B10  C10  D10
#      11  A11  B11  C11  D11


'''Конкатенация (соединение) нескольких DataFrame
   при этом должна совпвдать размерность в доль которой конкатенируем
   для столбцов: axis=1, для рядов оставляем по умолчанию axis=0'''

pd.concat([df1, df2, df3])
#           A    B    C    D
#     0    A0   B0   C0   D0
#     1    A1   B1   C1   D1
#     2    A2   B2   C2   D2
#     3    A3   B3   C3   D3
#     4    A4   B4   C4   D4
#     5    A5   B5   C5   D5
#     6    A6   B6   C6   D6
#     7    A7   B7   C7   D7
#     8    A8   B8   C8   D8
#     9    A9   B9   C9   D9
#     10  A10  B10  C10  D10
#     11  A11  B11  C11  D11

pd.concat([df1, df2, df3], axis=1)
#           A    B    C    D    A    B    C    D    A    B    C    D
#     0    A0   B0   C0   D0  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
#     1    A1   B1   C1   D1  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
#     2    A2   B2   C2   D2  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
#     3    A3   B3   C3   D3  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
#     4   NaN  NaN  NaN  NaN   A4   B4   C4   D4  NaN  NaN  NaN  NaN
#     5   NaN  NaN  NaN  NaN   A5   B5   C5   D5  NaN  NaN  NaN  NaN
#     6   NaN  NaN  NaN  NaN   A6   B6   C6   D6  NaN  NaN  NaN  NaN
#     7   NaN  NaN  NaN  NaN   A7   B7   C7   D7  NaN  NaN  NaN  NaN
#     8   NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN   A8   B8   C8   D8
#     9   NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN   A9   B9   C9   D9
#     10  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  A10  B10  C10  D10
#     11  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  A11  B11  C11  D11



'merge():'
''' merge(left: Any,
          right: Any,
          how: str = "inner",
          on: Any = None,      # по какому столбцу будем делать объединение
          left_on: Any = None,
          right_on: Any = None,
          left_index: bool = False,
          right_index: bool = False,
          sort: bool = False,
          suffixes: Tuple[Optional[str], Optional[str]] = ("_x", "_y"),
          copy: bool = True,
          indicator: bool = False,
          validate: Any = None) -> DataFrame
'''

df4 = pd.DataFrame({'order_id': [114, 235, 432],
                    'user_id': [1, 2, 3],
                    'user_name': ['James Brown', 'Jack White', 'Jane Green'],
                    'country': ['USA', 'USA', 'France']})

df5 = pd.DataFrame({'order_id': [114, 235, 432],
                    'user_id': [1, 2, 3],
                    'order_date': ['2020-02-11', '2020-02-11', '2020-02-15'],
                    'OS': ['Android', 'iOS', 'Android']})

'df4'
#       order_id  user_id    user_name country
#    0       114        1  James Brown     USA
#    1       235        2   Jack White     USA
#    2       432        3   Jane Green  France
'df5'
#       order_id  user_id  order_date       OS
#    0       114        1  2020-02-11  Android
#    1       235        2  2020-02-11      iOS
#    2       432        3  2020-02-15  Android

pd.merge(df4, df5, on='user_id')
#        order_id_x  user_id    user_name country  order_id_y  order_date       OS
#     0         114        1  James Brown     USA         114  2020-02-11  Android
#     1         235        2   Jack White     USA         235  2020-02-11      iOS
#     2         432        3   Jane Green  France         432  2020-02-15  Android

pd.merge(df4, df5, on='order_id')
#        order_id  user_id_x    user_name country  user_id_y  order_date       OS
#     0       114          1  James Brown     USA          1  2020-02-11  Android
#     1       235          2   Jack White     USA          2  2020-02-11      iOS
#     2       432          3   Jane Green  France          3  2020-02-15  Android

'если изменить значания в user_id (df5 на df7):'
df6 = pd.DataFrame({'order_id': [114, 235, 432],
                    'user_id': [1, 2, 3],
                    'user_name': ['James Brown', 'Jack White', 'Jane Green'],
                    'country': ['USA', 'USA', 'France']})

df7 = pd.DataFrame({'order_id': [114, 235, 432],
                    'user_id': [2, 4, 3],
                    'order_date': ['2020-02-11', '2020-02-11', '2020-02-15'],
                    'OS': ['Android', 'iOS', 'Android']})

#        order_id  user_id    user_name country
#     0       114        1  James Brown     USA
#     1       235        2   Jack White     USA
#     2       432        3   Jane Green  France

#        order_id  user_id  order_date       OS
#     0       114        2  2020-02-11  Android
#     1       235        4  2020-02-11      iOS
#     2       432        3  2020-02-15  Android
'мы получим только те ряды, в котором значения user_id одинаковы'
pd.merge(df6, df7, on='user_id')
#        order_id_x  user_id   user_name country  order_id_y  order_date       OS
#     0         235        2  Jack White     USA         114  2020-02-11  Android
#     1         432        3  Jane Green  France         432  2020-02-15  Android
'если сделать merge по двум столбцам, то мы получим стороки в которых значения этих столбцов одинаковы'
pd.merge(df6, df7, on=['user_id', 'order_id'])
#        order_id  user_id   user_name country  order_date       OS
#     0       432        3  Jane Green  France  2020-02-15  Android



'join()'

df8 = pd.DataFrame({'user_name': ['James Brown', 'Jack White', 'Jane Green'],
                    'country': ['USA', 'USA', 'France']},
                   index=['ind1', 'ind2', 'ind3'])

df9 = pd.DataFrame({'order_id': [114, 235, 432],
                    'user_id': [2, 4, 3],
                    'order_date': ['2020-02-11', '2020-02-11', '2020-02-15'],
                    'OS': ['Android', 'iOS', 'Android']},
                   index=['ind1', 'ind4', 'ind3'])

'df8'
#             user_name country
#     ind1  James Brown     USA
#     ind2   Jack White     USA
#     ind3   Jane Green  France
'df9'
#           order_id  user_id  order_date       OS
#     ind1       114        2  2020-02-11  Android
#     ind4       235        4  2020-02-11      iOS
#     ind3       432        3  2020-02-15  Android
'делаем join меняя местами df8 и df9, и получаем 2 разных результата:'
'NaN для тех столбцов где мы не имеем соотв. значений'
df8.join(df9)
#             user_name country  order_id  user_id  order_date       OS
#     ind1  James Brown     USA     114.0      2.0  2020-02-11  Android
#     ind2   Jack White     USA       NaN      NaN         NaN      NaN
#     ind3   Jane Green  France     432.0      3.0  2020-02-15  Android

df9.join(df8)
#           order_id  user_id  order_date       OS    user_name country
#     ind1       114        2  2020-02-11  Android  James Brown     USA
#     ind4       235        4  2020-02-11      iOS          NaN     NaN
#     ind3       432        3  2020-02-15  Android   Jane Green  France
