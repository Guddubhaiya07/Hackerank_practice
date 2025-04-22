# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N=int(input())
arr=[]
for i in range(N):
    a=list(map(float,input().split()))
    arr.append(a)
print(np.linalg.det(arr))
    
