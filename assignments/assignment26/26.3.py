# Arithmatic class

class Arithmatic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def accept(self):
        self.value1 = int(input("Enter the value of first Variable: "))
        self.value2 = int(input("Enter the value of second variable: "))

    def Addition(self):
        return  self.value1 + self.value2

    def Subtraction(self):
        return self.value1 - self.value2 

    def Product(self):
        return self.value1 * self.value2    

    def Division (self):
        if self.value2 == 0:
            print("Invlaid input")

        return self.value1 / self.value2
    
    def Display(self):
        print("Addition = ", self.Addition())
        print("Subtraction = ", self.Subtraction())
        print("Product = ", self.Product())
        print("Division = ", self.Division())

aobj1 = Arithmatic()
aobj2 = Arithmatic()

aobj1.accept()
aobj1.Addition()
aobj1.Subtraction()
aobj1.Product()
aobj1.Division()
aobj1.Display()

    




