import numpy as np
import pandas as pd

dframe = pd.read_csv('students.csv')
dframe_mean = dframe.iloc[:, 1:].mean(axis=1)
dframe['Средний'] = dframe_mean
dframe = dframe.sort_values('Средний', ascending=False)

dframe.to_excel('students_mean.xlsx', index=False)

print(dframe['Средний'].max())
print(dframe['Средний'].idxmax())
maxb = dframe['Средний'].max()
newf = dframe[dframe['Средний'] == maxb]
print(newf['Имя'])
