class Student:
    
    def __init__(self):
        self.name = "Raju"
        self.age = 25
    
    def update(self):
        self.age = 31
        
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
    

s1 = Student()
s2 = Student()

print("address of s1:", id(s1))
print("address of s2:", id(s2))

print("S1 name:", s1.name)
print("S1 age:", s1.age)
print("S2 name:", s2.name)
print("S2 age:", s2.age)

print("Calling update in s2 and changing value in s1")

s2.update()
s1.name = "Daniel"

print("S1 name:", s1.name)
print("S1 age:", s1.age)
print("S2 name:", s2.name)
print("S2 age:", s2.age)

if s1.age == s2.age:
    print("age is equal")
else:
    print("age is different")
    
print("updating s1 age")
s1.age = 31

if s1.age == s2.age:
    print("age is equal")
else:
    print("age is different")

print("Comparing s1 and s2. Is it same", s1.compare(s2))

print("Changing age of s2")
s2.age = 28

print("Compare s1 and s2. Is it same", s1.compare(s2))


