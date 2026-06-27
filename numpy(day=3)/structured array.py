import numpy as np
a = np.array([('aniket',22,67.8),('anivesh',21,54.5)])
print(a[0])
print(a[1])
b = np.array([('adi',22,67.8),('sunny',25,78.5)],dtype=[('name','U10'),('age','i4'),('weight','f4')])
print(b[0])
print(b[1])
print(b['name'])
print(b['age'])
print(b['weight'])
b[0][1]=23   #changing the age of adi from 22 to 23 
print(b[0])  
b['age']= 25
print(b)     #changing the age of all the records to 25
c = np.array([('adi',22,67.8),('sunny',25,78.5)],dtype={'name':['age','weight'],'formats':['U10','i4','f4']})
print(c['name'])