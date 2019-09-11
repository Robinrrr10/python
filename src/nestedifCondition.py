x = int(input("Enter any number:"))

if x % 2 == 0:
    print("number is even")
    if x > 5:
        print("number is greater than 5")
    else:
        print("number is less than 5")
else:
    print("number is odd")