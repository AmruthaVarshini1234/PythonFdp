'''m = (2 * 5) - 2
for i in range(0,5):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")'''


size=int(input("Enter the size: "))
for i in range(size):
    for space in range(size-i-1):
        print(" ",end=" ")

    for star in range (2*i+1):
        print("*",end=" ")
    print()

for i in range(size-2,-1,-1):
    # print(" ", end=" ")
    for space in range(size-i-1):
        print(" ", end=" ")
    for star in range (2*i+1):
        print("*", end=" ")
    print()
'''for i in range(size-2,-1,-1):
    print(" ", end=" ")
    for space in range(size+i-1):
        print("*", end=" ")
    for star in range (2*i-1-1):
        print(" ", end=" ")

    print()'''
