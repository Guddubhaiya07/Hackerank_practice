# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n,m=map(int,input().split())

a=[]
for i in range(n):
    a.append([*map(int,input().split())])
arr=numpy.array(a)
print(numpy.transpose(arr))
print(arr.flatten())
