class Parent:
    def __init__(self) -> None:
        print("init from parent")


class Child(Parent):
    def __init__(self) -> None:
        print("init from child")


p = Parent()
c = Child()
