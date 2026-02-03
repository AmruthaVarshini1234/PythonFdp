def add (a=None,b=None,c=None):
    if a!=None and b!=None and c!=None:
        result=a+b+c
    elif a!=None and b!=None:
        result=a+b
    else:
        result=a
    return result

print(add(1,2,3))
print(add(1,2,))
print(add(1))
