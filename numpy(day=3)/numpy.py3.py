# # import numpy as np 
# # a1 = np.arange(12)
# # print(a1)
# # a1 = a1.reshape(4,3)
# # print(a1)
# # a1 = np.arange(5,50,5)
# # print(a1)
# # a1 = np.arange(50,5,-5)
# # print(a1)
# # a1 = np.linspace(1,10,2)
# # print(a1)
# # a1 = np.linspace(1,10,3)
# # print(a1)

# import numpy as np
# a1 = np.array([ [1,2,3],[4,5,6],[7,8,9],[10,11,12]],dtype="float")
# print(a1)
# a1[1,1]=np.nan
# print(a1)
# a1 = np.identity(3,'int')
# print(a1)

import numpy as np
a1 = np.random.rand(4,3)
print(a1)
a1 = np.random.randint(10, size=(4,3))
print(a1)
