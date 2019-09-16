from cmath import pi
class Student:
    
    school = "CCM"
    
    def __init__(self, eng, tam, maths):
        self.eng = eng
        self.tam = tam
        self.maths = maths
        
    def average(self):
        return (self.eng + self.tam + self.maths)/3
    
    @classmethod
    def studentSchool(cls):
        return cls.school
    
    @staticmethod
    def info():
        return "Hi.how are you"
        
    
    
    

s1 = Student(45, 34,  61)
s2 = Student(78, 91, 83)
print("Average mark of s1:", s1.average())
print("Average mark of s2:", s2.average())
print("School name is:", Student.studentSchool())
print("Welcome message is:", Student.info())

