#Create a class called scheme with scheme_id, scheme_name,outgoing_rate, and message_charge.
# Derive customer class form scheme and include cust_id, name and mobile_no data.
# Define necessary functions to read and display data.

class scheme:

    def Scheme(self):
        self.scheme_id = int(input("Enter the Scheme Id : "))
        self.scheme_name = input("Enter the Scheme Name : ")
        self.outgoing_rate = float(input("Enter the Outgoing Rate : "))
        self.message_charge = float(input("Enter the Message Charge : "))


class customer(scheme):

    def cust_data(self):
        self.cust_id = int(input("Enter the Customer Id : "))
        self.cust_name = input("Enter the Customer Name : ")
        self.mobile_no = int(input("Enter the Mobile Number : "))


c = customer()
c.Scheme()
c.cust_data()
