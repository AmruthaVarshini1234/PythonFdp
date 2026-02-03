class India:
    def capital(self):
        print("Delhi")
class USA:
    def capital(self):
        print("Whashington D C")

objIndia = India()
objIndia.capital()
objUSA= USA()
objUSA.capital()


class additon1:
    def add(self,a,b):
        result=int(a+b)
        print(result)
class additon2:
    def add(self,a,b,c):
        result=int(a+b+c)
        print(result)
obj1= additon1()
obj2= additon2()
obj1.add(1,2)
obj2.add(3,4,5)

class additon3:
    def add(self,a,b,c):
        result=int(a+b+c)
        print(result)
    def add(self,a,b):
        result=int(a+b)
        print(result)

obj= additon3()
obj.add(1,2)
obj.add(3,4,5)


# obj= additon3()
# obj.add(1,2)
# obj.add(3,4,5)