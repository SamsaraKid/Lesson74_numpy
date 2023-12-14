
import numpy as np
import pandas as pd


data = {'Name': ['Boris', 'Max', 'Tomas', 'Robert'],
        'Age': [25, 35, 45, 65],
        'City': ['NY', 'LA', 'SPB', 'MSK']}

dframe = pd.DataFrame(data)
dframe.index = ['a', 'b', 'c', 'd']  # переименование строк
dframe.columns = ['A', 'B', 'C']  # переименование столбцов
print(dframe.loc['a', 'A'])  # получить ячейку по именам
print(dframe.iloc[0, 0])  # получить ячейку по индексу
print(dframe.loc['a'])  # строка а
print(dframe.loc[:, 'A'])  # столбец А
print(dframe['A'])  # столбец А

print('#########################################')

arr = np.random.randint(10, 99, size=(4, 4))
arrframe = pd.DataFrame(arr)
arrframe.columns = ['A', 'B', 'C', 'D']
arrframe.index = ['a', 'b', 'c', 'd']


dframe1 = pd.read_csv('data.csv')  # , encoding='windows-1251' , encoding='utf-8'
dsort_2 = dframe1.sort_values(by='столбец_2')
dsort_3 = dframe1.sort_values(by='столбец_3')

dframe1 = dframe1.drop(['столбец_1'], axis=1)

print('#########################################')

data1 = {'Name': ['Igor', 'Anna', 'Igor', 'Anna', 'Zahar'],
         'Money': [120, 130, 140, 105, 160]}
dframe2 = pd.DataFrame(data1)
newframe = dframe2.groupby(by='Name').sum()