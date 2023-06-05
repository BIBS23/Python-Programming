import numpy as np

a = np.array([8,3,3,4,8,9])
b= np.array([4,3,6,7,8,9])

s = np.add(a,b)
d = np.subtract(a,b)
p = np.multiply(a,b)
q = np.divide(a,b)
m = np.mod(a,b)


print('sum is ',s)
print('difference is ',d)
print('product is ',p)
print('quotient',d)
print(m)
