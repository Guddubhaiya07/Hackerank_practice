import numpy as np
n,m,p=list(map(int,input().split()))



l1=[]

for i in range(n+m):
    l1.append(list(map(int,input().split())))
    
arr1=np.array(l1)

print(arr1)
