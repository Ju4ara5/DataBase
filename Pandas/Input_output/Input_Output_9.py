import pandas as pd

'Работа с базой данных из файла cvs формата/ просмотреть такой файл можно с помощью соответствующего ридера'

pd.read_csv('us-500.csv')
#         first_name  ...                                      web
#     0        James  ...             http://www.bentonjohnbjr.com
#     1    Josephine  ...         http://www.chanayjeffreyaesq.com
#     2          Art  ...           http://www.chemeljameslcpa.com
#     3        Lenna  ...      http://www.feltzprintingservice.com
#     4      Donette  ...        http://www.printingdimensions.com
#     ..         ...  ...                                      ...
#     495    Brittni  ...                http://www.innerlabel.com
#     496    Raylene  ...                 http://www.hermarinc.com
#     497        Flo  ...   http://www.simontonhoweschneiderpc.com
#     498       Jani  ...  http://www.warehouseofficepaperprod.com
#     499   Chauncey  ...  http://www.affiliatedwithtravelodge.com
#
#     [500 rows x 12 columns]

'получаем первых 10 строк базы данных'
first_10_rows = pd.read_csv('us-500.csv').head(10)  # по умолчанию head(5)
type(first_10_rows)  # pandas.core.frame.DataFrame
#       first_name  ...                                    web
#     0      James  ...           http://www.bentonjohnbjr.com
#     1  Josephine  ...       http://www.chanayjeffreyaesq.com
#     2        Art  ...         http://www.chemeljameslcpa.com
#     3      Lenna  ...    http://www.feltzprintingservice.com
#     4    Donette  ...      http://www.printingdimensions.com
#     5     Simona  ...         http://www.chapmanrosseesq.com
#     6     Mitsue  ...       http://www.morlongassociates.com
#     7      Leota  ...         http://www.commercialpress.com
#     8       Sage  ...  http://www.truhlarandtruhlarattys.com
#     9       Kris  ...     http://www.kingchristopheraesq.com
#
#     [10 rows x 12 columns]

'создаем csv файл из 10 строк исходной DataFrame (index=False - без индексов)'
first_10_rows.to_csv('my_csv.csv', index=False)

'получаем значения первых 10 столбцов city'
pd.read_csv('us-500.csv').head(10)['city']
#     0    New Orleans
#     1       Brighton
#     2     Bridgeport
#     3      Anchorage
#     4       Hamilton
#     5        Ashland
#     6        Chicago
#     7       San Jose
#     8    Sioux Falls
#     9      Baltimore
#     Name: city, dtype: object


'EXCEL'
'''получаем данные из xlsx файла c указанием имени табличных данных (sheet_name='SalesOrders')
   если не указать этого, то получим результат из первой вкладки excel файла'''
df = pd.read_excel('SampleData.xlsx', sheet_name='SalesOrders')
#         OrderDate   Region       Rep     Item  Units  Unit Cost    Total
#     0  2018-01-06     East     Jones   Pencil     95       1.99   189.05
#     1  2018-01-23  Central    Kivell   Binder     50      19.99   999.50
#     2  2018-02-09  Central   Jardine   Pencil     36       4.99   179.64
#     3  2018-02-26  Central      Gill      Pen     27      19.99   539.73
#     4  2018-03-15     West   Sorvino   Pencil     56       2.99   167.44
#     5  2018-04-01     East     Jones   Binder     60       4.99   299.40
#     6  2018-04-18  Central   Andrews   Pencil     75       1.99   149.25
#     7  2018-05-05  Central   Jardine   Pencil     90       4.99   449.10
#     8  2018-05-22     West  Thompson   Pencil     32       1.99    63.68
#     9  2018-06-08     East     Jones   Binder     60       8.99   539.40
#     10 2018-06-25  Central    Morgan   Pencil     90       4.99   449.10
#     11 2018-07-12     East    Howard   Binder     29       1.99    57.71
#     12 2018-07-29     East    Parent   Binder     81      19.99  1619.19
#     13 2018-08-15     East     Jones   Pencil     35       4.99   174.65
#     14 2018-09-01  Central     Smith     Desk      2     125.00   250.00
#     15 2018-09-18     East     Jones  Pen Set     16      15.99   255.84
#     16 2018-10-05  Central    Morgan   Binder     28       8.99   251.72
#     17 2018-10-22     East     Jones      Pen     64       8.99   575.36
#     18 2018-11-08     East    Parent      Pen     15      19.99   299.85
#     19 2018-11-25  Central    Kivell  Pen Set     96       4.99   479.04
#     20 2018-12-12  Central     Smith   Pencil     67       1.29    86.43
#     21 2018-12-29     East    Parent  Pen Set     74      15.99  1183.26
#     22 2019-01-15  Central      Gill   Binder     46       8.99   413.54
#     23 2019-02-01  Central     Smith   Binder     87      15.00  1305.00
#     24 2019-02-18     East     Jones   Binder      4       4.99    19.96
#     25 2019-03-07     West   Sorvino   Binder      7      19.99   139.93
#     26 2019-03-24  Central   Jardine  Pen Set     50       4.99   249.50
#     27 2019-04-10  Central   Andrews   Pencil     66       1.99   131.34
#     28 2019-04-27     East    Howard      Pen     96       4.99   479.04
#     29 2019-05-14  Central      Gill   Pencil     53       1.29    68.37
#     30 2019-05-31  Central      Gill   Binder     80       8.99   719.20
#     31 2019-06-17  Central    Kivell     Desk      5     125.00   625.00
#     32 2019-07-04     East     Jones  Pen Set     62       4.99   309.38
#     33 2019-07-21  Central    Morgan  Pen Set     55      12.49   686.95
#     34 2019-08-07  Central    Kivell  Pen Set     42      23.95  1005.90
#     35 2019-08-24     West   Sorvino     Desk      3     275.00   825.00
#     36 2019-09-10  Central      Gill   Pencil      7       1.29     9.03
#     37 2019-09-27     West   Sorvino      Pen     76       1.99   151.24
#     38 2019-10-14     West  Thompson   Binder     57      19.99  1139.43
#     39 2019-10-31  Central   Andrews   Pencil     14       1.29    18.06
#     40 2019-11-17  Central   Jardine   Binder     11       4.99    54.89
#     41 2019-12-04  Central   Jardine   Binder     94      19.99  1879.06
#     42 2019-12-21  Central   Andrews   Binder     28       4.99   139.72

'сохраняем данные df в новый excel файл, с именем вкладки'
#df.to_excel('My_Excel.xlsx', sheet_name='MySheet')



'HTML'

html_data = pd.read_html('https://en.wikipedia.org/wiki/List_of_largest_cities')
type(html_data)  # list
'''Так как html_data является типом list, это значит что на веб-странице есть список таблиц, 
   чтоб получить оттуда DataFrame, нам надо указать индекс нужной нам таблицы.
   В нашем случае [1]'''
df1 = html_data[1]
type(df1)  # pandas.core.frame.DataFrame
#                              City[a]        Country  ... Urban area[8]
#                              City[a]        Country  ...     Area(km2) Density(/km2)
#     0                            NaN            NaN  ...           NaN           NaN
#     1                          Tokyo          Japan  ...        8231.0      4,751[e]
#     2                          Delhi          India  ...        2233.0     14,272[f]
#     3                       Shanghai          China  ...        4069.0      5,436[g]
#     4                      São Paulo         Brazil  ...        3237.0      6,949[h]
#     ..                           ...            ...  ...           ...           ...
#     77  Washington metropolitan area  United States  ...        5501.0      1,378[r]
#     78                        Yangon        Myanmar  ...         603.0         10774
#     79                    Alexandria          Egypt  ...         293.0         16577
#     80                         Jinan          China  ...         798.0          5490
#     81                   Guadalajara         Mexico  ...         313.0    17,371[22]
#
#     [82 rows x 13 columns]
'теперь с ней можно работать как с обычной DataFrame'
'сохраняем информацию в csv файл'
df1.to_csv('eu_big_city.csv')

'получаем данные в json формате'
json_data = df1.to_json()
