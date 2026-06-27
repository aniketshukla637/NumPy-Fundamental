# import numpy as np
# a1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(a1)
# print(np.sort(a1))
# print(int(a1.mean()))
# print(a1.diagonal())        #principal diagonal
# print(a1.trace())           #sum or principal diagonal
# print(a1.transpose())       #interchange of rows and columns
# print(a1.min())
# print(a1.max())
# print(np.ptp(a1))           #peak to peak (max-min)
# print(a1.sum())
# print(a1.prod())            #product of all elements
# print(a1.std())             #standard deviation(square root of variance)
# print(a1.var())             #variance(average of squared deviations from mean)
# print(a1.ndim)
# print(a1.shape)               #ye bol rha hai ki 2d ke ander kitne dimentions hai and uske bhi ander kitne elements hai
# print(a1.reshape(1,9))
# print(a1.size)              #no. of elements is = size

# import numpy as np
# a1 = np.array([1,2,3,4,5,6,7,8])
# a2 = a1.copy()
# a1[0]=2
# print(a1)                    #sirf ismai he change hoga
# print(a2)
# a2 = a1.view()
# a1[0]=3
# print(a1)                    #dono mai change hoga
# print(a2)

# import numpy as np 
# c1 = np.array([[5,4,1],[2,3,6],[7,8,9]])
# print(c1)
# print(np.sort(c1))       
# print(c1.reshape(1,9))
# c1=np.ones((3,3),int)         #ye sabko one mai convert kar dega 
# print(c1)
# c1=np.full((3,3),2,int)       #ye 2 kar dega sabko aise he kisi mai bhi change kara sakte hai
# print(c1)

