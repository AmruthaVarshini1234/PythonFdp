mylist=[1,2,3,4,5]
anotherlist=list(range(2,101,2))
print (anotherlist)
print (mylist[0])
for i in mylist:
    print (i)
print(anotherlist[0:10])
for i in range(8,11):
    mylist.append(i)
print(mylist)
mylist.insert(5,50)
print(mylist)
mylist.insert(1,"hello world")
print(mylist)
mylist.remove(50)
print(mylist)
mylist.reverse()
print(mylist)
# mylist.sort()
print(mylist)
mylist.pop()
print(mylist)
del mylist[0]
print(mylist)
del mylist[1]
print(mylist)
mylist.pop()
print(mylist)
mylist.sort()
print(mylist)
mylist[2]=40
print(mylist)
