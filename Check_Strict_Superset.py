'''You are given a set  and  other sets.
Your job is to find whether set  is a strict superset of each of the  sets.

Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example
Set is a strict superset of set.
Set is not a strict superset of set.
Set is not a strict superset of set.'''


a=set(map(int,input().split()))
b=int(input())
c=True
for i in range(b):
    d=set(map(int,input().split()))
    if not (a.issuperset(d) and a != d):
        c= False
    
print(c)


