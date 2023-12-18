import pandas as pd

data = [35000, 600, 3000, 2000]
names = ['jan', 'feb', 'mar', 'apr']
ser = pd.Series(data, index=names)
print(ser.sum())
print(ser['mar'])
print(ser.mar)

print('####################')

data2 = [100000, 120000, 150000, 80000, 200000, 250000, 180000, 300000, 280000, 320000, 350000, 400000,
        180000, 200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000, 360000, 380000, 400000,
        150000, 300000, 250000, 280000, 320000, 350000, 380000, 400000, 420000, 440000, 470000, 500000,
        200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000, 360000, 380000, 400000, 420000,
        150000, 160000, 180000, 200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000, 360000]


ser2 = pd.Series(data2, index=pd.date_range(start='2019-01-01', periods=len(data2), freq='M'))

sumYears = ser2.groupby(ser2.index.year).sum()
meanYears = ser2.groupby(ser2.index.year).mean().round(0)
print(meanYears)

print('####################')

maxYear = sumYears.idxmax()
