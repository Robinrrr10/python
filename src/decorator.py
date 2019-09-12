from _ctypes_test import func
def div(a ,b):
    return a / b

print("4 divided by 2 is:", div(4, 2))
print("2 divided by 4 is:", div(2, 4))

def check_div(func):
    def check(a,b):
        if(a < b):
            a, b = b, a
        return func(a,b)
    return check
div = check_div(div)
print("4 divided by 2 is:", div(4, 2))
print("2 divided by 4 is(Here it should always divides with greater to small):", div(2, 4))