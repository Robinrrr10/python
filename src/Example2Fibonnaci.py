def fib(count):
    a = 0
    b = 1
    if count == 1:
        print(a)
    else:
        print(a)
        print(b)
        
        for i in range(2, count):
            c = a + b
            print(c)
            a, b =  b, c

fib(int(input("Enter number of fibonnaci number:")))