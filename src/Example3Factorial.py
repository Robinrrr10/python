def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    print("Factorial of ", num, " is:", result)

n = int(input("Enter number:"))
factorial(n)