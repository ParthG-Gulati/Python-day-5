#Create a class cal3 that will calculate simple interest.
# Create constructor method which has three parameters .
# Create calInterest() method that will calculate Interest .
# Create display() method that will display Interest.

class cal3:
    prin=0
    rate=0
    time=0
    interest=0

    def __init__(self):
        self.prin=float(input("Enter the principle amount:"))
        self.rate=float(input("Enter the rate:"))
        self.time=float(input("Enter the time duration:"))

    def calInterest(self):
        self.interest = ((self.prin)*(self.rate)*(self.time))/100

    def display(self):
        print("For principle amount of:"+ str(self.prin) +"\trate:" + str(self.rate) + "\ttime duration:" + str(self.time) + "yrs\nThe simple interest is: " + str(self.interest))

int = cal3()
int.calInterest()
int.display()

