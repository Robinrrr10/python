class Student:
    
    school = "daniel Tomas"  # this is class variable. This is static variable
    
    def __init__(self):
        self.name = "Rahul"
        self.age = 45

s1 = Student()
s2 = Student()
print("s1 name is:", s1.name, " age:", s1.age, " school:", s1.school)
print("s2 name is:", s2.name, " age:", s2.age, " school:", s2.school)

Student.school = "Jayarajesh"

print("s1 name is:", s1.name, " age:", s1.age, " school:", s1.school)
print("s2 name is:", s2.name, " age:", s2.age, " school:", s2.school)
