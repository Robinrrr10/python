def factorial(n):
    if n==0:
        return 1
    return n * factorial(n -1)

result = factorial(5)
print("Factorial of 5 is:", result)