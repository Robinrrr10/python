class Student:
    def set_name(self, name): # This is accessor. setter
        self.name = name
        
    def get_name(self): # This is mutator. getter
        return self.name
    
c1 = Student()
c2 = Student()

c1.set_name("Dinesh")
print("Name is:", c1.get_name())
