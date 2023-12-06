import numpy as np

income = np.array([[1000000, 2000000, 2500000, 3000000, 2150000],
                    [1560000, 2330000, 2500000, 3990000, 2150000],
                    [2120000, 2500000, 3770000, 2650000, 4000000],
                    [2589000, 2990000, 4488000, 4586000, 3500000],
                    [2100000, 2599000, 3100000, 2110000, 4233000],
                    [1533000, 2660000, 4220000, 3500000, 2577000]])

cities = np.array(['Нижний Новгород', 'Астрахань', 'Самара', 'Москва', 'Воронеж', 'Санкт-Петербург'])
datas = np.array(['10.07.23', '11.07.23', '12.07.23', '13.07.23', '14.07.23'])

sumSTR = np.sum(income, axis=1)
sumSTR = sumSTR.reshape(6, 1)
maxCity = np.argmax(sumSTR)
print(cities[maxCity])

sumCOL = np.sum(income, axis=0)
maxData = np.argmax(sumCOL)
print(cities[maxData])

newT = income.T