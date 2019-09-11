n = [11, 34, 23, 14, 89, 20, 65,47, 29]
for i in n:
    if i % 3 == 0:
        print("first number divisible by 3 is:", i)
        break
else:   # will will work only if for loop contains break statement. if break statement is not used this will work
    print("none of the number divisible by 3")

print("done")