arr = tuple(map(int, input().split()))
a=[]
for i in arr:
    a.append(arr.count(i))

s=0
for j in a: 
    if j > 1: 
        s += 1

print(False if s > 1 else True)
