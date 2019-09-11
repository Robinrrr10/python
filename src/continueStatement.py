k = int(input("What divisible number it should not print:"))
for i in range(1,30):
    if(i % k == 0):
        continue
    print("number is:", i)
print("done")