# method overloading is not supported in python. but we can achieve by a trick

class Student:
    def add(self, a=None, b=None, c=None):
        result = None
        if a!=None and b!=None and c!=None:
            result = a + b + c
        elif a!=None and b!=None:
            result = a + b
        else:
            result = a
        return result
    
s1 = Student();
print("Addition result:", s1.add(5))
print("Addition result:", s1.add(10, 34))
print("Addition result:", s1.add(8, 2, 7))