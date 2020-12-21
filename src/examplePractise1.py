print("Hi Hello")
a = 1
b = 4.3
c = True
d = "mynam"
print(a, b, c, d)
age = int(input("Enter your age"))
if age > 18 and age < 25 :
    print("Eligible")
elif age >= 25 and age <= 30:
    if age == 27:
        print("Special age...")
    print("Perfect age")
else:
    print("Old age")

res = a + b
print(res)

tah = 2 ** 2
print("tah is:", tah)
print(type(tah))

name = "raju tHN mAn arE"
print("upper:", name.upper())
print("Lower:", name.lower())
print("Capitlize:", name.capitalize())
print("number of char:",len(name))
print("number of r:", name.count("r"))
print("hi" * 3)

lst = [78, 12, False, "maa", 2, "just"]
for each in lst:
    print(each)
print("len is:", len(lst))
lst.append(891)
print(lst[6])
lst2 = lst
lst.extend(lst2)
print(lst)
print(lst2)
lst3 = lst[2:7]
print(lst3)

mytur = (34, 12, 98, 12, 44, 28, 74, 8, 11, 45)
for i in mytur:
    print(i)
for j in range(10):
    print(j)

for k in range(2, 20, 3):
    print(k)

mytur2 = ("ji", "hh", "hello", "this")
for inx, val in enumerate(mytur2):
    print(inx , " is:", val)

lst4 = [78, "huuu", 23, True, 9.2, "jhn"]
sl1 = lst4[2:4:1]
print(sl1)

st1 = set()
print(type(st1))
s2 = {56, 78, 23, 90, 78, 12, 54, 11, 90, 11}
print(s2)
s3 = {87, 50, 67}
print(s2.union(s3))
dis = {'name': "ram", "age": 24}
print(dis['age'])
dis['name'] = "damm"
print(dis)
