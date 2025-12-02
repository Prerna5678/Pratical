class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def disp1(self):
        print(self.name)
        print(self.age)


class Child(Parent):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def disp2(self):
        print(self.salary)


p = Parent("Surat", 28)
p.disp1()

print("*" * 30)
c = Child("Guj", 20, 90000)
c.disp2()
c.disp1()
