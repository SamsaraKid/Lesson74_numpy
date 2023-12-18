import pandas as pd

data = pd.read_csv('sales_data.csv')

data2 = data['Количество'].tolist()
dates = data['Дата'].tolist()

ser = pd.Series(data2, index=dates)

ser2 = pd.Series(data.Количество.values, index=data.Дата.values)