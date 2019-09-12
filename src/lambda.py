from _functools import reduce
nums = [2, 7, 4, 9, 5, 3, 8]

evens = lambda n : n%2==0
allEvens = list(filter(evens, nums)) 
print("Even numbers are :", allEvens)

evenNumbers = list(filter(lambda n: n%2==0, nums))
print("Even numbers are(using lambda directly):", evenNumbers)

squareOfNums = list(map(lambda n: n*n, nums))
print("Suare of each numbers are:", squareOfNums)

sumOfNums = reduce(lambda a,b : a+b, nums)
print("Sum of all numbers are:", sumOfNums)