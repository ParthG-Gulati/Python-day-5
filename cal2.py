#Create a class cal2 that will calculate area of a circle.
# Create setdata() method that should take radius from the user.
# Create area() method that will calculate area . Create display() method that will display area .

import math

class cal2():
    radius = 0
    area = 0

    def setdata(self):
        self.radius = float(input("Enter the value of radius of circle"))

    def area(self):
        self.area = math.pi*(self.radius**2)

    def display(self):
        print("The area of circle with radius\t" +str(self.radius) +"\tis :" +str(self.area))

ca = cal2()
ca.setdata()
ca.area()
ca.display()

