# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
np.set_printoptions(legacy='1.13')
a=list(map(float,input().split()))
q=np.array(a)
print(np.floor(q))
print(np.ceil(q))
print(np.rint(q))
