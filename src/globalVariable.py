a = 10
print("global variable a is:", a)
def demo():
    a = 15
    print("local variable a is:", a)
demo()
print("again global variable a is:", a)

b = 13
def demo2():
    print("global variable b inside function is:", b)
demo2()
print("global variable b is:", b)


c = 7
print("global variable c is:", c)
def demo3():
    global c
    c = 5
    print("changed global variable c inside function is:", c)
demo3()
print("again global variable c is:", c)

d = 14
print("global variable d is", d)
print("address of global variable d is:", id(d))
def demo4():
    d = 19
    print("local variable d is:", d)
    e = globals()['d']
    print("global variable d is assigned to e:", e)
    print("address of e is:", id(e))
    globals()['d'] = 22
demo4()
print("again global variable d is:", d)

