n = 10
b = int(input("At what number it should break:"))
i = 1;
while i <= n:
    if i == b:
        break
    print("Number is:", i)
    i = i + 1
print("done")