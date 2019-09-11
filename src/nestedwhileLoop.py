name = input("Enter any name:")
count = int(input("How many times the name should print:"))
noOfStar = int(input("How many stars are required in end of each name:"))
i = 1
while i <= count:
    print("\n", name, end="")
    j = 1
    while j <= noOfStar: 
        print("*", end="")
        j = j + 1
    i = i + 1

print("\nThanks")
