def leepyear(year):
    if year%100==0:
        if   year%400!=0:
              return False
        elif year%4:
            return True
        else:
            return True
    elif year%4==0:
        return True
    else:
        return False
a=int(input())
print(leepyear(a))
