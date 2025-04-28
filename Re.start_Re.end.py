import re
s=input()
k=input()
matches=list(re.finditer(f'(?={k})',s))
if not matches:
    print((-1,-1))
else:
    for match in matches:
        print((match.start(),match.start()+len(k)-1))

