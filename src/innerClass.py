
class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print("Name:", self.name, " and age:", self.age)
        
    class laptop:
        def __init__(self, brand, ram):
            self.brand = brand
            self.ram = ram
        def display(self):
            print("Laptop brand:", self.brand, " and Ram:", self.ram)
            
    
s1 = Student('arun', 26)
s2 = Student('navin', 21)
s1.display()
s2.display()

lap1 = s1.laptop("Sony", 8)
lap2 = s2.laptop("Mac", 16)

lap1.display()
lap2.display()