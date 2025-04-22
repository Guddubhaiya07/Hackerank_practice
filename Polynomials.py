# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
P=list(map(float,input().split()))
arr=np.array(P)
x=int(input())
print(np.polyval(arr,x))
