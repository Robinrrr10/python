
class Student:
    def __init__(self):
        print("This is the constructor")
    
    def school(self):
        print("This is my school")

std1 = Student()
std1.school()

class Employee:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
    
    def empDetail(self):
        print("Name of employee:" + self.name + " and designation:" + self.designation)

emp1 = Employee("Ragu", "HR")
emp1.empDetail()
emp2 = Employee("Babu", "Product Manager")
emp2.empDetail()