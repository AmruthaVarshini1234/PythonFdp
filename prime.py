'''n=int(input("Enter a number: "))
is_prime=True
if  n<2:
    is_prime=False
else:
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
print("prime"if is_prime else "not prime")'''

n=int(input("Enter a number: "))
for i in range(1,n):
    if i%i==0 or i%1==0 or (n%i)==0:
        print(f"{i} is prime")
    else:
        print(f"{i} is not prime")