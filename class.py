#Create a class cal1 that will calculate sum of three numbers.
#Create setdata() method which has three parameters that contain numbers.
#Create display() method that will calculate sum and display sum.


class cal1():
    n1 = 0
    n2 = 0
    n3 = 0
    def setdata(self):
        self.n1 = int(input("Enter number 1"))
        self.n2 = int(input("Enter number 2"))
        self.n3 = int(input("Enter number 3"))

    def display(self):
        sum = self.n1 + self.n2 + self.n3
        print("The sum is:", sum)


sum = cal1()
sum.setdata()
sum.display()


