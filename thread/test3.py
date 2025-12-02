class Parent:
    def disp1(self):
        print("Disp1 from parent")

    def show(self):
        print("show from parent")


class Child(Parent):
    def disp2(self):
        print("Disp2 from child")

    def show(self):
        print("show from child")


p = Parent()
c = Child()

p.disp1()
p.show()
print("*" * 25)
c.disp1()
c.disp2()
c.show()
