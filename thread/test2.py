class Parent:
    def disp1(self):
        print("Disp1 from parent")


class Child(Parent):
    def disp2(self):
        print("Disp2 from child")


p = Parent()
c = Child()

p.disp1()
print("*" * 25)
c.disp1()
c.disp2()
