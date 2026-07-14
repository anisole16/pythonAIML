# implement circle with following requirement


class Circle:
    PI = 3.142

    def __init__(self):
        self.radius = 0
        self.area = 0
        self.circumference = 0

    def accept(self):
        self.radius = int(input("Enter the radius of the circle: "))  

    def CalculateArea(self):
        self.area = Circle.PI * self.radius * self.radius

    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    def Display(self):
        print("Radius = ", self.radius)
        print("Area = ", self.area)
        print("Circumferene = ", self.circumference)
        print()


cobj1 = Circle()
cobj2 = Circle()

print("Enter Circle1 Parameters")
cobj1.accept()
cobj1.CalculateArea()
cobj1.CalculateCircumference()
cobj1.Display()

print("Enter Circle2 Parameters")
cobj2.accept()
cobj2.CalculateArea()
cobj2.CalculateCircumference()
cobj2.Display()



