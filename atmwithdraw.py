balance=50000
w=int(input("enter the amount you want to withdraw:"))
if balance>w:
    balance=balance-w
    print(balance)
if balance<0:
    print("you cannot withdraw negative amount")
if w>balance:
        print("you cannot withdraw amount is out of balance")

