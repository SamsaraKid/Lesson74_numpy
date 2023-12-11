import numpy as np

data = np.genfromtxt(fname='litecoin.csv', delimiter=',', skip_header=1, usecols=(1, 4))
maxdata = np.max(data, axis=0)
nummax = np.argmax(data, axis=0)

import pandas as pd

newdata = pd.read_csv('litecoin.csv')
print(newdata)
print(newdata.describe())

datas = newdata['Date']

print('in first col max', nummax[0], datas[nummax[0]], 'equal', maxdata[0])
print('in second col max', nummax[1], datas[nummax[1]], 'equal', maxdata[1])