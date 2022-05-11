
class Student:

    def dispaly(self):
        print("print things")

s1 = Student()
s1.dispaly()

s2 = Student()
Student.dispaly(s2)

class Emp:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dis(self):
        print("Name is: ", self.name, " Age is:", self.age)

k = Emp("Rahul", 25)
k.dis()

k2 = Emp("Thani", 78)
k2.dis()

nm = 8
print(nm)
class Man:
    nm = 5
    print(nm)
    def change(self):
        nm = 3
        print(nm)

mm = Man()
mm.change()

print(nm)

jk = 78
class Just:
    def chan(self):
        global jk
        jk=56

jj = Just()
jj.chan()
print(jk)

class AA:
    def aa(self):
        print("AA")

class BB(AA):
    def bb(self):
        print("BB")

a = AA()
a.aa()

b = BB()
b.bb()
b.aa()

class CC:
    def cc(self):
        print("CC")

class DD(AA,CC):
    def dd(self):
        print("DD")

print("llllllllllllllllll")
d = DD()
d.aa()
d.cc()
d.dd()

n1 = 6
n2 = 9
print("n1=", n1, " n2=", n2)
n1,n2 = n2,n1
print("n1=", n1, " n2=", n2)

# This is command

'''This is documentation
    we can use like this'''
def hoho():
    print("kkkkk")

hoho()

class MM:
    def my(self):
        print("mm")

class KK(MM):
    def my(self):
        print("kk")

m1 = MM()
m1.my()

k8 = KK()
k8.my()

def add(a = None, b = None, c = None):
    if a != None and b != None and c != None:
        return a + b + c
    elif a != None and b != None:
        return a + b
    else:
        return a


print("Addition", add(9, 2, 1))
print("Addition",add(9, 2))
print("Addition",add(9, ))

