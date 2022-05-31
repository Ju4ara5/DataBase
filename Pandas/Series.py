import numpy as np
import pandas as pd

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
np_arr = np.array(numbers)  # [1 2 3]
dict1 = {'a': 1, 'b': 2, 'c': 3}

''' Аргументы в  Series:
            (data: Any = None,
             index: Any = None,
             dtype: Any = None,
             name: Any = None,
             copy: bool = False,
             fastpath: bool = False) -> None'''

pd.Series(data=numbers)  # 0    1     (индекс -> значение)
                         # 1    2
                         # 2    3
                         # dtype: int64  (значения типа int)

pd.Series(data=numbers, index=letters)  # a    1  (в индексах список букв)
                                        # b    2
                                        # c    3
                                        # dtype: int64

'''Если передавать параметры (аргументы) Series в нужнои порядке
   то необязательно указывать тип, и пример выше можно записать так:
   pd.Series(numbers, letters)
   результат будет тотже.'''

pd.Series(np_arr)  # 0    1
                   # 1    2
                   # 2    3
                   # dtype: int32

pd.Series(np_arr, letters)  # a    1
                            # b    2
                            # c    3
                            # dtype: int32

pd.Series(letters)  # 0    a
                    # 1    b
                    # 2    c
                    # dtype: object  (значения типа str по этому теперь object)

'из словаря:'
pd.Series(dict1)  # a    1
                  # b    2
                  # c    3
                  # dtype: int64


life_long = pd.Series([84.7, 84.5, 83.7],
                      ['Honk kong', 'Japan', 'Singapore'])  # Honk kong    84.7
                                                            # Japan        84.5
                                                            # Singapore    83.7
                                                            # dtype: float64     (значения типа float)

life_long_1 = pd.Series([84.7, 84.5, 83.7],
                      ['USA', 'Japan', 'Singapore'])

'Сумируются только значения у которых одинаковый индекс, в другом варианте вернет NaN'
life_long + life_long_1  # Honk kong      NaN
                         # Japan        169.0
                         # Singapore    167.4
                         # USA            NaN
                         # dtype: float64

'Обращение к элементу серии через индекс:'
x = life_long['Japan']  # 84.5
