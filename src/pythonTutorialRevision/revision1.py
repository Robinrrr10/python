print('Hi')

print(1+2)

print("hi", 343)

a = 5
print(a)
b = 5.4
print(b)
c = "hi hello"
print(c)
d = True
print(d)
e = None
print(e)
f = [4, 5, 89, 12, "heh", 78.1, True, 23, 11]
print(f)
g = {13, 3, 12, 51, 17, 17, 15, 48}
print(g)
h = {"name": "ram", "mark": 89}
print(h)


def addSub(a, b):
    return a+b, a-b

res1, res2 = addSub(25, 15)
print("result 1:", res1, " result 2:", res2)

def pt(s, h):
    print("s is:", s, " h is:", h)

pt(45, 12)
pt(h=45, s=12)
