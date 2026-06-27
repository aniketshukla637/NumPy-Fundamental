#lecture = 4 se he main numpy start 

#check time to execution
# import numpy as np
# import time
# m = 10000
# m1 = [[e for e in range(m)] for i in range(m)]
# m2 = [[e for e in range(m)] for i in range(m)]
# start = time.time()
# m1 = np.array(m1)
# m2 = np.array(m2)
# m1+m2
# end = time.time()
# print("%.6f seconds "%(end-start))   

#arrays banana
# import numpy as np
# a = np.array([1,2,3])
# print(a)

#fast calculations
# import numpy as np
# arr = np.array([1,2,3])
# print(arr +2)
# print(arr*3)

#matrix operations important for ai ,ml
# import numpy as np
# a = np.array([[1,2 ,3],[4,5,6]])
# b = np.array([[7,8,9],[10,11,12]])
# print(a+b)
# print(a*b)

#statistics nikalma
# import numpy as np
# a = np.array([10,20,30,])
# print(np.mean(a))
# print(np.max(a))
# print(np.min(a))

#random data genrate karna
# import numpy as np
# print(np.random.rand(2))      
      
#shape & dimentions handle karna 
# import numpy as np
# arr = np.array([[1,2,3],[4,5,6]])   
# print(np.shape(arr))
      
#reshape means data ko change karna 
# import numpy as np
# arr = np.array([[1,2,3,4,5,6]])
# print(arr.reshape(2,3))   
             

#check that list fast or arrays
# import time
# from tracemalloc import start
# n = 10000
# m1 = [[e for e in range(n)] for i in range(n)]
# m2 = [[e for e in range(n)] for i in range(n)]
# start = time.time()
# for i in range(n):
#     for j in range(n):
#         m1[i][j]+m2[i][j]
# end = time.time()   
# print("%.6f seconds "%(end-start))    // list takes running 19.983992 seconds
                                        #//done time 35.591

# import time

# import numpy as np
# n= 10000
# m1 = np.array([[e for e in range(n)]for i in range(n)])
# m2 = np.array([[e for e in range(n)]for i in range(n)])
# start=time.time()
# m1 = np.array(m1)
# m2 = np.array(m2)
# m = m1+m2
# end = time.time()                    // numpy takes running 0.894617 seconds
# print("%.6f seconds "%(end-start))   //done time 19.897
