

def welcomeMsg():
    print("Welcome to python")

welcomeMsg()
welcomeMsg()

def sub(a, b):   
    c = a - b
    print("Substraction result is:", c)

def add(a, b): # with return type
    c = a + b
    return c

def add_and_multiply(a, b):  
    j = a + b
    k = a * b
    return j, k    # returning multiple value

sub(18, 13)
adres = add(7, 8)
print("addition result is:", adres)
print("addition result is:", add(16, 14))

addresult, multiresult = add_and_multiply(5, 4)
print("addition result:", addresult, ", multiplication result:", multiresult)



