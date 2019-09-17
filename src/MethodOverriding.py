class Employee:
    def salary(self):
        print("average salary is 50000")

class Hrs(Employee):
    def salary(self):
        print("average salary of HR is 72000")
        
        
h1 = Hrs()
h1.salary()

e1 = Employee()
e1.salary()

        