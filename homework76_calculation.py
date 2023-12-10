import numpy as np

 # Январь, Февраль, Март, Апрель, Май, Июнь, Июль, Август, Сентябрь, Октябрь, Ноябрь, Декабрь
x = [[1000, 1200, 1500, 1350, 1400, 1300, 1250, 1450, 1300, 1550, 1600, 1700], # Завод 1
    [800, 900, 1000, 950, 1000, 1100, 1200, 1150, 1000, 1100, 1200, 1300], # Завод 2
    [1200, 1300, 1250, 1400, 1500, 1600, 1650, 1700, 1600, 1550, 1500, 1400], # Завод 3
    [900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450]]# Завод 4

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

print('Sum of bicycles =', np.sum(x))
sumSTR = np.sum(x, axis=1)
for i, s in enumerate(sumSTR):
    print(f'Factory {i + 1} produce {s} bicycles in year')
print('Best factory is', np.argmax(sumSTR) + 1)
print('Best month is', months[np.argmax(np.sum(x, axis=0))])

