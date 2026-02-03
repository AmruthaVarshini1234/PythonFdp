from itertools import repeat

mytuple = (10,20,30,'bmsce')
print(mytuple)
anothertuple =tuple(range(10))
print(anothertuple)
print(mytuple[0])
print(mytuple[3])
print(mytuple[-1])
print(mytuple[1:3])
result=mytuple+anothertuple
print(result)
repeatedtuple = mytuple*3
print(repeatedtuple)
print(3 in mytuple)
print(3 in anothertuple)
print(3 not in mytuple)
print(len(mytuple))
print(mytuple.count(10))
print(anothertuple.count(9))
print(mytuple.index("bmsce"))
