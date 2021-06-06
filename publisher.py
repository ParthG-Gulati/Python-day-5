#Write a program with use of inheritance: Define a class publisher that stores the name of the title.
# Derive two classes book and tape, which inherit publisher.
# Book class contains member data called page no and tape class contain time for playing.
# Define functions in the appropriate classes to get and print the details.

class publisher:

    def Name(self):
        self.title = input("Enter the title of the book:")


class book(publisher):

    def data(self):
        self.pageNum = int(input("Enter the number of pages of the book:"))


class tape(publisher):

    def timeForPlaying(self):
        self.time = float(input("Enter the time for playing:"))


a = book()
b = tape()

a.Name()
a.data()
b.timeForPlaying()