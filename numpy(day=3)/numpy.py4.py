import numpy as np
# a1 = np.array([10,20,30,40,50])
# print(a1)
# print(a1[0],a1[1],a1[2],a1[3],a1[4])
# print(a1[-1],a1[-2],a1[-3],a1[-4],a1[-5])
# a1 = np.array([[4,5],[6,7]])
# print(a1)
# print(a1[0])
# print(a1[1])
# print(a1[0,0])
# print(a1[1,1])
# a1 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(a1)
# print(a1[0])
# print(a1[1])
# print(a1[0,0,0])
# print(a1[0,0,1])
# print(a1[1,0,0])
# print(a1[-0])
# print(a1[-1])

# a1 = np.array([1,2,3,4,5,6,7,8])
# print(a1[1:4:2])
# print(a1[1:])
# print(a1[:])
# print(a1[::1])
# print(a1[::-1])

#college work
#read full content 
with open("students.txt","w") as f:
    f.write("Amit,20, Delhi\n")
    f.write("Neha,22,Mumbai\n")
    f.write("Rahul,19,kolkata\n")
    f.write("Priya,21,chennai\n")
with open("students.txt","r") as f:
    print(f.read())
print("\n")    
#read first line 
with open("students.txt","r") as f:
    print("\n",f.readline())
print("\n")
#read all lines in list
with open("students.txt","r") as f:
    print("\n",f.readlines())
print("\n")
#read line by line
with open("students.txt","r") as f:
    for line in f:
        print(line.strip())
print("\n")
#count no. of students
with open("students.txt","r") as f:
    print("no. of students",len(f.readlines()))
print("\n")    
#overwrite content
with open("students.txt","w")as f:
    f.write("anivesh,21,lucknow\n")
    f.write("akshat,10,mumbai\n")

with open("students.txt","r") as f:
    print(f.read())
print("\n")            
#append new student
with open("students.txt","a")as f:
    f.write("aditya,23,lucknow\n")

with open("students.txt","r") as f:
    print(f.read())
print("\n")
#update first students name
with open("students.txt","r+") as f:
    data = f.readlines()
    data[0] = data[0].replace("anivesh","aniket shukla")
    f.seek(0)
    f.writelines(data)

with open("students.txt","r") as f:
    print(f.read())    
#add sneha at end using r+
with open("students.txt","r+") as f:
    f.seek(0, 2)
    f.write("sneha , 18, hydrabad\n")
with open("students.txt","r") as f:
    print(f.read())  
      