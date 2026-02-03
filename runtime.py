class mom:
    def cook(self):
        print("indian cook")


class daughter(mom):
    def cook(self):
        print("chinese cook")
        pass
    def bake(self):
        print("cake")
m=mom()
d=daughter()
m.cook()
d.cook()
d.bake()