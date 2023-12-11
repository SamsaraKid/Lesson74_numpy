import numpy as np
import pandas as pd

years = np.random.randint(2010, 2024, size=(100000, 1))
sales = np.random.randint(500, 1500, size=(100000, 1))
income = np.random.randint(50000, 150000, size=(100000, 1))

data = np.concatenate((years, sales, income), axis=1)
newdata = data[data[:, 0] == 2018]
sum18sales = np.sum(newdata[:, 1])
sum18income = np.sum(newdata[:, 2])

df = pd.DataFrame(data)
print(df)
print(df.columns)
df2 = df.groupby(0).sum()
# print(df2)
maximums = df2.idxmax(axis='rows')
print('max sales in:', maximums[1])
print('max income in:', maximums[2])