#Consider an employee class, which contains fields such as name and designation.
#And a subclass, which contains a field salary.# Write a program for inheriting this relation.

class employee:
    name = ""
    designation = ""

    def NAME(self):
        self.name = input("Enter the name of the Employee:")

    def DESIGNATION(self):
        self.designation = input("Enter the designation of the Employee:")


class salary(employee):
    salary=0.0

    def SALARY(self):
        self.salary = int(input("Enter the salary of the Employee:"))

sal=salary()
sal.NAME()
sal.DESIGNATION()
sal.SALARY()