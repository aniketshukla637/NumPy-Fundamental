import numpy as np 
a1 = np.array([1,2,3])
print(a1+1)
print(a1.shape)
a2 = np.array([4,5,6])
a3 = np.array([[1],[2],[3]])
print(a2+a3)        #a2 is 1D and a3 is 2D, but they can be added together because of broadcasting
print(a2.shape)
print(a3.shape)

