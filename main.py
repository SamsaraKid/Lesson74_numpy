import numpy as np


a = np.array([1, 2, 3, 4, 5])
print(a)

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)

c = np.arange(0 ,10)
print(c)

d = np.random.rand(3, 3)
print(d)

e = np.zeros((3, 5))
print(e)

m1 = np.random.randint(1, 9, size=(3, 3))
m2 = np.random.randint(1, 9, size=(3, 3))
print(m1)
print(m2)
m3 = m1 + m2
print(m3)
maxM = np.max(m3)
minM = np.min(m3)
sumM = np.sum(m3)
avgM = np.average(m3)

print(maxM, minM, sumM, avgM)