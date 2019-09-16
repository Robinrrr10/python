class A:

    def afeature1(self):
        print("This is feature 1 from a")   
        
    def afeature2(self):
        print("This is feature 2 from a")  
        
class B(A):   # Single inheritace
    
    def bfeature3(self):
        print("This is feature 3 from b")   
        
    def bfeature4(self):
        print("This is feature 4 from b")
        
class C(B):   # multi level inheritance
    
    def cfeature5(self):
        print("This is feature 5 from c")   
        
    def cfeature6(self):
        print("This is feature 6 from c")
        
class D:
    
    def dfeature7(self):
        print("This is feature 7 from d")   
        
    def dfeature8(self):
        print("This is feature 8 from d")
        
class E(A,D):  # multiple inhertance
    
    def efeature9(self):
        print("This is feature 9 from e")   
        
    def efeature10(self):
        print("This is feature 10 from e")
        
a = A()
a.afeature1()
a.afeature2()

b = B()  # Single level inheritance
b.afeature1()
b.afeature2()
b.bfeature3()
b.bfeature4()

c = C()   # multi level inheritance
c.afeature1()
c.afeature2()
c.bfeature3()
c.bfeature4()
c.cfeature5()
c.cfeature6()

e = E()  # multi level inheritance
e.afeature1()
e.afeature2()
e.dfeature7()
e.dfeature8()
e.efeature9()
e.efeature10()



        
        
        
        
