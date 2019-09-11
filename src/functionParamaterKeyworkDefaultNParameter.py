def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Rahul", 16)
student(age=23, name="Kumar") #using keyword age and name

def person(name, age=18): #default is 18 if age is not passed
    print("Name:", name)
    print("Age:", age)

person("ram")
person("Dinesh", 14)

def addAllValues(*n): # this will accept n number of values. Accually it is turple
    result = 0
    for i in n:
        result = result + i
    print("Sum of all values is:", result)

addAllValues(3, 1, 5, 1)
addAllValues(2, 81, 3)

def employee(name, **data):
    print("Name is:", name)
    for i,j in data.items():
        print(i, j)

employee("Rahul", age=27, mobile=989878882, depart="cse")
employee("Arul", email="arun2@gmail.com",age=45)