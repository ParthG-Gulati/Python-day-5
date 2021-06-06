#Create a class cal4 that will calculate square of a number.
#Create setdata() method which has one parameters that contain number.
#Create display() method that will calculate sum.(Function should return value)

class cal4:
    n = 0
    square = 0

    def setdata(self):
        self.n = int(input("Enter the number:"))

    def display(self):
        self.square = (self.n)**2
        print("Square is :", self.square)

sq=cal4()
sq.setdata()
sq.display()
