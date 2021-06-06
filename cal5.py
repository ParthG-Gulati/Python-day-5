#Create a class cal5 that will calculate area of a rectangle.
# Create constructor method which has two parameters.
# Create calArea() method that will calculate area of a rectangle.
# Create display() method that will display area of a rectangle.

class cal5:
    len = 0
    brd = 0
    area = 0

    def __init__(self):
        self.len = float(input("Enter the length:"))
        self.brd = float(input("Enter the breadth:"))

    def calArea(self):
        self.area = self.len * self.brd

    def display(self):
        print("The area of the rectangle is:" + str(self.area))

ar = cal5()
ar.calArea()
ar.display()
