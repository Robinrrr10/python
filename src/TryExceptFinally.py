print("This is division")
numtop = input("Enter top number:")
numBottom = input("Enter bottom number:")


try:
    print("mysql connection openned")
    tnum = int(numtop)
    bnum = int(numBottom)
    result = tnum / bnum
    print("division result is:", result)
except ValueError as e:
    print("Invalid input. error:", e)
except ZeroDivisionError as e:
    print("Any number cannot  be divisible by zero. error:", e)
except Exception as e:
    print("Something went wrong....")
finally:
    print("mysql connection closed")
