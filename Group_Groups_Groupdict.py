import re
s=re.search(r'([a-zA-Z0-9])\1',input())

if s:
    print(s.group()[0])
else:
    print("-1")
         

