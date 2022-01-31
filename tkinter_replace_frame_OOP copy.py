class Parent(object): #This is a Borg class
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.valueA = 5


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.valueB = 10

    def Calculate(self):
        self.result = self.valueB + self.valueA
        print(self.result)


class MainProgram():
    def __init__(self):
        self.parent = Parent()
        self.child = Child()

        self.parent.valueA = 8

        self.child.Calculate()

foobar=MainProgram()