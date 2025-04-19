import re
a=int(input())
#check=re.match(r'^[7|8|9]\d{9}$')
for _ in range(a):
    s=input()
    if re.match(r'^[789]\d{9}$', s):
        print('YES')
    else:
        print('NO')
