a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number"))
if a>b and a>c:
    print(" {} is greater than {} and {}".format(a,b,c))
elif b>c:
        print(" {} is greater".format(b))
else:
        print(" {} is greater".format(c))
