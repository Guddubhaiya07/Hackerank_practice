# Enter your code here. Read input from STDIN. Print output to STD
import numpy as np
n=int(input())

A=[]
B=[]
for i in range(n):
    a=list(map(int,input().split()))
    A.append(a)
arr1=np.array(A)
for i in range(n):
    b=list(map(int,input().split()))
    B.append(b)
arr2=np.array(B)
print(np.dot(arr1, arr2))
#print(np.cross(arr1, arr2))
