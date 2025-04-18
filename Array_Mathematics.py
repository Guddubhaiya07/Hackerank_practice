import numpy as np
n,m = map(int,input().strip().split(' '))
a=[]
b=[]
#for i in range(n):
a=np.array([list(map(int,input().split(' '))) for _ in range(n)])
b=np.array([list(map(int,input().split(' '))) for _ in range(n)])
    
q = a #numpy.array(a, float)
w =  b #numpy.array(b, float)
print(np.add(q, w))
print(np.subtract(q, w))
print(np.multiply(q, w))
h=np.divide(q, w)
print(h.astype(int))
print(np.mod(q, w))
print(np.power(q, w))   
