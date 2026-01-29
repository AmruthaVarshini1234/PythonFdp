a=10
b=20.5
print(type(a),a)
print(type(b),b)
c=a+b
print(type(c),c)
Birthyear=int(input("Enter your birthyear: "))
print(type(Birthyear),Birthyear)
currentyear=int(input("Enter your current year: "))
print(type(currentyear),currentyear)
age=currentyear-Birthyear
print("your age is:"+str(age))
print(f"your age is:{age}")
# formatted strings
print("{} years old".format(age))
print("{} years old".format(age))