print("starting")

def add(a, b):
    return a + b, a - b

x, y = add(10, 6)
print("X:", x, " Y:", y)

def complex(*n, **m):
    print("st")
    print(n)
    print(*n)
    print(m)
    print(**m)
    print("en")

n = [34, 78, 12, 78]
m = {'name':'ram', "age": 20}
complex(n,m)

f = 12
class Student:
    k = 45
   
    def check(self):
        k = 23
        global f
        f = 51

st1 = Student()
st1.check()
print(st1.k)
print(f)

class MyClass:
    def __init__(self):
        print("my constructor")

m1 = MyClass()


class CheckClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def prt(self):
        print("p start")
        print(self.x, self.y)

ck1 = CheckClass(13, 56)
ck1.prt()