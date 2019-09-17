# +  operator will internally it will call __add__ method
# -, *. / will call __sub__, __mul__ and __div__ methods respectively



class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        j1 = self.m1 + other.m1
        j2 = self.m2 + other.m2
        res = Student(j1, j2)
        return res
    def __gt__(self, other):
        a = self.m1 + self.m2
        b = other.m1 + self.m2
        if a > b:
            return True
        else:
            return False
    
a = 15
b = 20
print("c is:", a + b) # here a will internally calls __add__ method
print("again c is:", int.__add__(a, b))
    
s1 = Student(23, 89)
s2 = Student(56, 76)
s3 = s1 + s2
print("s3 m1:", s3.m1, " m2:", s3.m2)

print("Which is greater:", s1 > s2)
print("Which is greater:", s2 > s1)