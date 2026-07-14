# implement a class named Demo with the following specifications

class Demo:
    Value = 100

    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def fun(self):
        print("Inside Fun Function !")
        print(self.no1)
        print(self.no2)

    def gun(self):
        print("Inside Gun Function !")
        print(self.no1)
        print(self.no2)

dobj1 = Demo(11, 21)
dobj2 = Demo(51, 101)

dobj1. fun()
dobj1.gun()


dobj2.fun()
dobj2.gun()

    

