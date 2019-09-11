# different methods of swap
print("-------------method 1-------------")
x = 5
y = 9
print("before swap")
print("x is:", x)
print("y is:", y)
tmp = x
x = y
y = tmp
print("After swap")
print("x is:", x)
print("y is:", y)
print("----------------------------------")

print("-------------method 2-------------")
x = 5
y = 9
print("before swap")
print("x is:", x)
print("y is:", y)
x = x + y
y = x - y
x = x - y 
print("After swap")
print("x is:", x)
print("y is:", y)
print("----------------------------------")

print("-------------method 3-------------")
x = 5
y = 9
print("before swap")
print("x is:", x)
print("y is:", y)
x,y = y,x
print("After swap")
print("x is:", x)
print("y is:", y)
print("----------------------------------")
