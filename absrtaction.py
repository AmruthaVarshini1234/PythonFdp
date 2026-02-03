class animal:
    def eat(self):
        print("eat")
class dog(animal):
    def bark(self):
        print("bark")
class puppy(animal):
    def sleep(self):
        print("sleep")


a=animal()
a.eat()
d=dog()
d.bark()
p=puppy()
p.eat()

