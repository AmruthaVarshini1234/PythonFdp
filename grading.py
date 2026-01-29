sub1=int(input("enter first sub marks: "))
sub2=int(input("enter second sub marks: "))
sub3=int(input("enter third sub marks: "))
sub4=int(input("enter fourth sub marks: "))
sub5=int(input("enter fifth sub marks: "))
if (0 < sub1 <= 100 and 0 < sub2 <= 100 and
    0 < sub3 <= 100 and 0 < sub4 <= 100 and
    0 < sub5 <= 100):
    print("All marks are between 0 and 100")
    total=sub1+sub2+sub3+sub4+sub5
    print(total)
    percentage=float(total/500)*100
    print(percentage)
    if percentage>=75:
        print(" grade is A")
    elif 50<=percentage>75:
        print(" grade is B")
    elif 30<=percentage>50:
        print(" grade is c")
    elif percentage<30:
        print("Fail")
else:
    print("invalid")




