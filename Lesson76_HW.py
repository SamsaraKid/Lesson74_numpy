import numpy as np
years = np.random.randint(2010,2024,size=(100000,1))
sales = np.random.randint(500,1500,size=(100000,1))
income = np.random.randint(50000, 150000, size=(100000, 1))

data = np.concatenate((years, sales, income), axis=1)
newdata = data[data[:,0]==2010]
sum10sales = np.sum(newdata[:,1])
sum10inc = np.sum(newdata[:,2])

groupdata = np.array([2010, sum10sales, sum10inc])
for year in range(2011, 2024):
    newdata = data[data[:, 0] == year]
    sumsales = np.sum(newdata[:, 1])
    suminc = np.sum(newdata[:, 2])
    groupdata = np.vstack([groupdata, np.array([year, sumsales, suminc])])

print(f'Max sales {groupdata[:, 1].max()} is in {groupdata[groupdata[:, 1].argmax(), 0]}')
print(f'Max income {groupdata[:, 2].max()} is in {groupdata[groupdata[:, 2].argmax(), 0]}')



# import pandas as pd
# df=pd.DataFrame(data)
# print(df)
# print(df.columns)
# df2=df.groupby(0).sum()
# print(df2[1].max())
# print(df2[2].max())
# maximums = df2.idxmax(axis="rows")
# # df2sort = df2.sort_values(by='1')
# print('больше продаж в ',maximums[1])
# print('больше выручка в ',maximums[2])
