class A:
    def __init__(self):
        print("init of A")
    def feature1(self):
        print("feature 1 in A")

class B(A):
    def feature2(self):
        print("feature 2 in B")

class C(A):
    def __init__(self):
        print("init of C")
    def feature3(self):
        print("feature 3 in C")
        
class D(A):
    def __init__(self):
        super().__init__()
        print("init of D")
    def feature4(self):
        print("feature 4 in D")

class E(C):
    def __init__(self):
        super().__init__()
        print("init of E")
    def feature5(self):
        print("feature 5 in E")

class F:
    def __init__(self):
        print("init of F")
    def feature6(self):
        print("feature 6 in F")
    def feature1(self):
        print("feature 1 in F")

class G(A,F):  # first priority to A. which is first right
    def __init__(self):
        super().__init__()
        print("init of G")
    
a1 = A()
b1 = B()
c1 = C()
d1 = D()
d1.feature1()
e1 = E()
g1 = G()
g1.feature1()
